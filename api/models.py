from django.db import models
import uuid
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

""" Название приложения, Ключ AP"""


class ApiKey(models.Model):
    key = models.UUIDField(default=uuid.uuid4, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class App(models.Model):
    name = models.CharField(max_length=255)
    keys = models.ManyToManyField(ApiKey)
