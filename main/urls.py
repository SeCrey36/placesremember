from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.redirect_to_dashboard, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_memory, name='create_memory'),
    path('memory/<int:memory_id>/', views.view_and_edit_memory, name='view_and_edit_memory'),
    path('memory/delete/<int:memory_id>/', views.delete_memory, name='delete_memory'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', views.logout, name='logout'),
]
