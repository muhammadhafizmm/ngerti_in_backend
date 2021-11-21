# from pathlib import Path
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
# from django.utils.timezone import localtime, now
# from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    no_hp = models.CharField(max_length=13, blank=True, default="")
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ["email", "is_staff", "is_superuser"]

    def __str__(self):
        return self.username


class Jurusan(models.Model):
    name = models.CharField(max_length=25, blank=True, default="")
    
    def __str__(self):
        return self.name
    

class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student",
    )
    jurusan = models.ForeignKey(
        Jurusan, 
        on_delete=models.SET_NULL,
        related_name="jurusan",
        null=True
        )
    
    is_premium = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
