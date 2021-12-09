from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tryout import views as tryout_views

tryout_router = DefaultRouter()
tryout_router.register(r"tryout", tryout_views.TryOutViewSet)

urlpatterns = [
    path("", include(tryout_router.urls)),
    path('<int:pk>/', include(tryout_router.urls))
]