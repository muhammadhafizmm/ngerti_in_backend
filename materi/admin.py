from django.contrib import admin
from .models import (
    Materi, Soal
)
# Register your models here.

admin.site.register(Materi)
admin.site.register(Soal)
