from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.todos import viewsets

router = DefaultRouter()
router.register('tasks', viewsets.TasksViewSet, basename='tasks')
router.register('auth', viewsets.AuthViewSet, basename='auth')

urlpatterns = [
    path('', include(router.get_urls()), name='tasks'),
]
