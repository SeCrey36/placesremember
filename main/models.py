from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    vk_id = models.CharField(max_length=100, unique=True)
    avatar_url = models.URLField(max_length=200)

class Memory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    comment = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    