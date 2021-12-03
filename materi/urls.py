from django.urls import path, include
from rest_framework.routers import DefaultRouter

from materi import views as materi_views

materi_router = DefaultRouter()
materi_router.register(r"jurusan",materi_views.JurusanViewSet)
materi_router.register(r"mapel",materi_views.MapelViewSet)
materi_router.register('soal', materi_views.SoalController, basename='soal')


urlpatterns = [
    path("", include(materi_router.urls)),
    path('<int:pk>/', include(materi_router.urls))
]
