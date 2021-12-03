from django.urls import path
from django.urls.conf import include 
from .views import MateriController, SoalController 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('materi', MateriController, basename='materi')
router.register('soal', SoalController, basename='soal')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/', include(router.urls)),
]