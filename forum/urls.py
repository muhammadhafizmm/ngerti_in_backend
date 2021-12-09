from django.urls import path, include
from rest_framework.routers import DefaultRouter

from forum import views as forum_views

forum_router = DefaultRouter()
forum_router.register(r"post",forum_views.ForumViewSet)

urlpatterns = [
    path("", include(forum_router.urls))
]
