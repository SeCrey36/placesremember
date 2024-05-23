from django.contrib import admin
from .models import CustomUser, Memory

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'vk_id', 'avatar_url')

@admin.register(Memory)
class MemoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'latitude', 'longitude', 'created_at')
