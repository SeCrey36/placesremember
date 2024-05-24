from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Memory

class MemoryCreationTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='secrey', password='A$12df341212', vk_id='123456', avatar_url='https://example.com/avatar.jpg')

    def test_memory_creation(self):
        memory = Memory.objects.create(user=self.user, title='Test Memory', comment='This is a test memory', latitude=56.7532444, longitude=34.9184423)
        self.assertEqual(memory.title, 'Test Memory')


class MemoryListViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        Memory.objects.create(user=self.user, title='Test Memory', comment='Just a test', latitude=0, longitude=0)

    def test_dashboard_view(self):
        # Выполняем запрос к странице dashboard
        response = self.client.get(reverse('dashboard'))
        # Проверяем, что ответ успешен (код 200)
        self.assertEqual(response.status_code, 200)
        # Проверяем, что на странице содержится текст 'Test Memory'
        self.assertContains(response, 'Test Memory')
