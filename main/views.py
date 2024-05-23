from django.shortcuts import render
from django.urls import reverse
from .models import CustomUser, Memory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect


@login_required
def dashboard(request):
    user = request.user
    memorys = Memory.objects.filter(author=user)
    links = []
    for memory in memorys:
        url = reverse('view_or_edit_article', kwargs={'memory_id': memory.pk})
        links.append({'title': memory.title, 'url': url})
    return render(request, 'account/dashboard.html', {'links': links})
    
    
@login_required 
def create_memory(request):
    pass
    # if request.method == 'POST':
    #     form = ArticleForm(request.POST)
    #     if form.is_valid():
    #         article = form.save(commit=False)
    #         article.author = request.user
    #         article.save()
    #         return redirect('dashboard')
    # else:
    #     form = ArticleForm()
    # return render(request, 'create_article.html', {'form': form})
    

# @login_required 
# def view_and_edit_memory(request, article_id):
#     article = get_object_or_404(Article, pk=article_id)
#     user = request.user
#     articles = Article.objects.filter(author=user)
#     links = []
#     for article in articles:
#         url = reverse('view_or_edit_article', kwargs={'article_id': article.pk})
#         links.append({'title': article.title, 'url': url})
#     if request.user == article.author:
#         if request.method == 'POST':
#             form = ArticleForm(request.POST, instance=article)
#             if form.is_valid():
#                 form.save()
#                 return redirect('view_or_edit_article', article_id=article_id)
#         else:
#             form = ArticleForm(instance=article)
#         return render(request, 'view_article.html', {'form': form, 'article': article, 'links': links})
#     else:
#         return render(request, 'view_article.html', {'article': article, 'links': links})
    

def logout(request):
    auth_logout(request)
    return redirect('/')