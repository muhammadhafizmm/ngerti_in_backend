from django.contrib import admin

# Register your models here.
from .models import (
    Materi,
    Modul,
    Mapel,
    Soal
)
# Register your models here.

admin.site.register(Mapel)
admin.site.register(Modul)
admin.site.register(Materi)
admin.site.register(Soal)
