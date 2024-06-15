from django.urls import path
from rest_framework.permissions import AllowAny

from users.apps import UsersConfig
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import UserViewSet, PaymentsViewSet, UserCreateAPIView

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'payments', PaymentsViewSet, basename='payments')

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
              ] + router.urls
