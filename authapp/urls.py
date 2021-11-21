from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authapp import views as user_account_views

user_account_router = DefaultRouter()
user_account_router.register(r"users",user_account_views.UserViewSet)
user_account_router.register(r"student",user_account_views.StudentViewSet)


urlpatterns = [
    path("", include(user_account_router.urls))
]
