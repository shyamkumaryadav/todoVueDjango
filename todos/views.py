from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from todos import serializers, models


class IsUserSame(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated|IsUserSame]

    def get_queryset(self):
        user = self.request.user.id
        return User.objects.filter(id=user)

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TodoSerializer
    # queryset = models.Todo.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.todo_set.all()