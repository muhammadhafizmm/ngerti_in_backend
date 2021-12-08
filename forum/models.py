from typing import Tuple
from django.db import models
from materi.models import (Mapel)
from authapp.models import (User)

# Create your models here.
class Post(models.Model):
    topik = models.CharField(max_length=100, blank=False)
    isi = models.TextField(blank=True, default="")
    waktu = models.DateTimeField(auto_now=True)
    mata_pelajaran = models.ForeignKey(
        Mapel, 
        related_name="mata_pelajaran",
        on_delete=models.CASCADE
    )
    pengirim = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="pengirim"
    )
    parent_post = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        related_name="parent",
        blank=True, 
        null=True
    )
    
    def __str__(self):
        return self.topik
