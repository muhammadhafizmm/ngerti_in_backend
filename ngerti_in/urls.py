"""ngerti_in URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView
from authapp.views import (
    RegisterView,
    LoginView,
)
from .views import index

authpatterns=[
    path('login', LoginView.as_view(), name="login"),
    path('register/', RegisterView.as_view(), name="register-student"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token-verify")
]

urlpatterns = [
    path('', include('authapp.urls')),
    path('belajar/', include('materi.urls')),
    path('auth/', include(authpatterns)),
    path('admin/', admin.site.urls),
    path('checkserver/', index, name='index'),
    path('to/', include('tryout.urls')),
]
