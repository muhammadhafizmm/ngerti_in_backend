from rest_framework import permissions

from authapp.models import Student
from .models import Mapel

class IsJurusan(permissions.BasePermission):
    def __init__(self):
        super().__init__()
        self.student_model = Student
        # self.teacher_model = Teacher
        
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            student = self.student_model.objects.filter(user=request.user.id)
            if student.exists():
                if student[0].jurusan.id == int (request.get_full_path().split("/")[-2]):
                    return True
        return False
    
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)

class IsMapelJurusan(permissions.BasePermission):
    def __init__(self):
        super().__init__()
        self.student_model = Student
        self.mapel_model = Mapel
    
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            student = self.student_model.objects.filter(user=request.user.id)
            if student.exists():
                mapel_id = request.get_full_path().split("/")[-2]
                mapel = self.mapel_model.objects.filter(id=mapel_id)
                if student[0].jurusan.id == (mapel[0].jurusan.id):
                    return True
        return False
    
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)