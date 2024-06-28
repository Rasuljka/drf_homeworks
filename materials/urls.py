from django.urls import path
from rest_framework.routers import SimpleRouter

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from materials.apps import MaterialsConfig
from materials.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonDestroyAPIView,
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView, SubscriptionCreateAPIView,
)

app_name = MaterialsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lessons/", LessonListAPIView.as_view(), name="lessons-list"),
    path("lessons/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lessons-retrieve"),
    path("lessons/create/", LessonCreateAPIView.as_view(), name="lessons-create"),
    path("lessons/<int:pk>/update/", LessonUpdateAPIView.as_view(), name="lessons-update"),
    path("lessons/<int:pk>/delete/", LessonDestroyAPIView.as_view(), name="lessons-delete"),
    path('subs/create/', SubscriptionCreateAPIView.as_view(), name='subs_create'),
]

urlpatterns += router.urls
