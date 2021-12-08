from django.urls import path, include
from rest_framework.routers import DefaultRouter

from materi import views as materi_views

materi_router = DefaultRouter()
materi_router.register(r"jurusan",materi_views.JurusanViewSet)
materi_router.register(r"mapel",materi_views.MapelViewSet)
materi_router.register(r"materi",materi_views.MateriController)
materi_router.register(r"soal",materi_views.SoalController)
materi_router.register(r"hasil",materi_views.HasilKuisController)

urlpatterns = [
    path("", include(materi_router.urls)),
    path('<int:pk>/', include(materi_router.urls))
]
