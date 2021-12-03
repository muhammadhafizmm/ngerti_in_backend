from django.db import models
from authapp.models import (
    Jurusan,
    
) 

# Create your models here.
class Mapel(models.Model):
    jurusan = models.ForeignKey(
        Jurusan,
        on_delete=models.CASCADE,
        related_name="rumpun"
    )
    name = models.CharField(max_length=50, blank=True, default="")
    
    def __str__(self):
        return self.name

class Modul(models.Model):
    mapel = models.ForeignKey(
        Mapel, 
        related_name="mapel",
        on_delete=models.CASCADE
    )
    name=models.CharField(max_length=50, blank=True, default="")
    
    def __str__(self):
        return self.name

class Materi(models.Model):
    modul = models.ForeignKey(
        Modul, 
        related_name="modul",
        on_delete=models.CASCADE
    )
    judul=models.CharField(max_length=50, blank=True, default="")
    materi=models.TextField(blank=True, default="")
    datetime=models.DateTimeField(auto_now_add=True)
    
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

    