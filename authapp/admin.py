from django.contrib import admin
from .models import (
    User,
    Student,
    Jurusan,
    Pengajar,
)
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Jurusan)
admin.site.register(Pengajar)