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
        post = self.get_object()
        user = request.user
        _, is_like = models.UserLike.objects.get_or_create(user=user, post=post)
        if is_like:
            return Response({'status': 'Vote Set'}, 
                            status=status.HTTP_200_OK)
        else:
            return Response({'status': 'Vote Not Set'},
                            status=status.HTTP_202_ACCEPTED)
    
    @set_vote.mapping.delete
    def unset_vote(self, request, slug=None):
        "delete the vote on the post"
        post = self.get_object()
        user = request.user
        _, is_like = models.UserLike.objects.get(user=user, post=post)
        return Response({"status": "delete me ok"}, status=status.HTTP_200_OK)