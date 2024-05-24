from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .forms import MemoryForm
from .models import CustomUser, Memory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect


def redirect_to_dashboard(request):
    return redirect('dashboard')

@login_required
def dashboard(request):
    user = request.user
    memories = Memory.objects.filter(user=user)
    links = []
    for memory in memories:
        url = reverse('view_and_edit_memory', kwargs={'memory_id': memory.pk})
        links.insert(0,{
            'id': memory.pk,
            'title': memory.title,
            'url': url,
            'latitude': memory.latitude,
            'longitude': memory.longitude,
            'created_at': memory.created_at,
            'comment': memory.comment
        })
    return render(request, 'account/dashboard.html', {'links': links})
    
    
@login_required
def create_memory(request):
    if request.method == 'POST':
        form = MemoryForm(request.POST)
        if form.is_valid():
            memory = form.save(commit=False)
            memory.user = request.user
            memory.save()
            return redirect('dashboard')
    else:
        form = MemoryForm()
    return render(request, 'memorys/create.html', {'form': form, 'error': 1})
    

@login_required
def view_and_edit_memory(request, memory_id):
    memory = get_object_or_404(Memory, pk=memory_id)
    user = request.user
    if user == memory.user:
        if request.method == 'POST':
            form = MemoryForm(request.POST, instance=memory)
            if form.is_valid():
                form.save()
                return redirect('dashboard')
        else:
            form = MemoryForm(instance=memory)
        return render(request, 'memorys/edit.html', {'memory': memory, 'form': form})
    else:
        return redirect_to_dashboard()
    
    
@login_required
def delete_memory(request, memory_id):
    if request.method == 'DELETE':
        memory = get_object_or_404(Memory, pk=memory_id, user=request.user)
        memory.delete()
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Invalid request method'}, status=405)
    

def logout(request):
    auth_logout(request)
    return redirect('/')