from django.contrib.auth import login, logout
from django.middleware.csrf import rotate_token
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from apps.todos.mixins import SerializerMapMixin
from apps.todos import serializers


class AuthViewSet(GenericViewSet):
    permission_classes = ()

    @action(detail=False, url_path='login', methods=['post'],
            serializer_class=serializers.LoginSerializer)
    def login(self, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request=self.request, user=user)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, url_path='logout', methods=['get'])
    def logout(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            logout(self.request)
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, url_path='restore_session', methods=['get'],
            serializer_class=serializers.UserSerializer)
    def restore_session(self, *args, **kwargs):
        csrf_cookie = self.request.META.get('CSRF_COOKIE', None)
        if not csrf_cookie:
            rotate_token(self.request)
        is_authenticated = self.request.user.is_authenticated
        serializer = self.get_serializer(instance=self.request.user)
        data = {
            'is_authenticated': is_authenticated,
            'user': serializer.data
        }
        return Response(data)


class TasksViewSet(SerializerMapMixin, ModelViewSet):
    serializer_class = serializers.TaskSerializer
    serializer_map = {
        'list': serializers.TaskListSerializer
    }

    def get_queryset(self):
        return self.request.user.tasks.all()

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
