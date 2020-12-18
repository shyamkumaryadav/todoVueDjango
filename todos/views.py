from rest_framework import permissions as rest_permissions
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.decorators import action
from rest_framework import viewsets, status
from todos import serializers, models
from rest_framework import mixins
from todos import permissions


class UserViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.UserSerializer
    permission_classes = [rest_permissions.IsAuthenticated&permissions.IsAuthor]
    queryset = User.objects.all()
    # lookup_field = "username"

    # def list(self, request, *args, **kwargs):
    #     data = {'status': 'welcome sir!'}
    #     try:
    #         if request.user.is_staff:
    #             queryset = self.filter_queryset(self.get_queryset())
    #             page = self.paginate_queryset(queryset)
    #             if page is not None:
    #                 serializer = self.get_serializer(page, many=True)
    #                 return self.get_paginated_response(serializer.data)

    #             serializer = self.get_serializer(queryset, many=True)
    #             data['user list'] = serializer.data
    #         elif request.user.is_authenticated: 
    #             data['url'] = self.get_serializer(request.user).data.get('url')
    #             data['username'] = self.get_serializer(request.user).data.get('username')
    #             data['first_name'] = self.get_serializer(request.user).data.get('first_name')
    #             data['last_name'] = self.get_serializer(request.user).data.get('last_name')
    #         else:
    #             return Response(data, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    #     except: pass
    #     return Response(data, status=200)
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    # def update(self, request, *args, **kwargs):
    #     return super(UserViewSet, self).update(request, *args, **kwargs)

    @action(detail=True, methods=['post'], serializer_class=serializers.UserPasswordSerializer)
    def set_password(self, request, pk=None):
        print("*"*10, "password chabgeing", "*"*10)
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TodoSerializer
    # queryset = models.Todo.objects.all()
    permission_classes = [rest_permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.todo_set.all()

class UserPostViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserPostSerializer
    queryset = models.UserPost.objects.all()
    permission_classes = [permissions.IsUserAdminPost]
    lookup_field = "slug"

    @action(detail=True, methods=['post'], permission_classes = [rest_permissions.IsAuthenticated])
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
            return Response({"detail": "Not found."},
                            status=status.HTTP_404_NOT_FOUND)
    
    @set_vote.mapping.delete
    def unset_vote(self, request, slug=None):
        "delete the vote on the post"
        post = self.get_object()
        user = request.user
        get_object_or_404(models.UserLike, user=user, post=post).delete()
        return Response({"status": "Vote unset"}, status=status.HTTP_200_OK)