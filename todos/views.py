from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from todos import serializers, models


class IsUserSame(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class IsUserAdminPost(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff

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

class UserPostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserPostSerializer
    queryset = models.UserPost.objects.all()
    permission_classes = [IsUserAdminPost]
    lookup_field = "slug"

    @action(detail=True, methods=['post'])
    def set_vote(self, request, slug=None):
        """
        I am set the vote count by 1.
        """
        post = self.get_object() and False
        print(post)
        if post:
            return Response({'status': 'password set'})
        else:
            return Response(self.serializer_class.errors,
                            status=status.HTTP_400_BAD_REQUEST)