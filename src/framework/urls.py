from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from src.framework.auth.views import AuthViewSet
from src.framework.user.views import UserViewSet

router = DefaultRouter()

router.register(r"api/auth", AuthViewSet, basename="auth")
router.register(r"api/users", UserViewSet, basename="user")

urlpatterns = [
    path("admin/", admin.site.urls),
] + router.urls
