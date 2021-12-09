from django.conf import settings
from django.db import models
from django.db.models.base import Model

# Create your models here.

class TryOut(models.Model):
    paket_try_out = models.CharField(max_length=30)
    file_soal = models.FileField()
    durasi_pengerjaan = models.IntegerField()

    def __str__(self):
        return self.paket_try_out
