# from pathlib import Path
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.base import Model
# from django.utils.timezone import localtime, now
# from django.utils.translation import gettext_lazy as _

# Create your models here.

class Materi(models.Model):
    judul = models.CharField(max_length=100, default="")
    isi = models.TextField(max_length=100, default="")
    
    def __str__(self):
        return self.judul

class Soal(models.Model):
    materi = models.ForeignKey(Materi, on_delete=models.CASCADE, related_name='soal')
    pertanyaan = models.TextField()
    A = models.TextField(default="")
    B = models.TextField(default="")
    C = models.TextField(default="")
    D = models.TextField(default="")
    E = models.TextField(default="")
    jawaban_benar = models.CharField(max_length=1)

    