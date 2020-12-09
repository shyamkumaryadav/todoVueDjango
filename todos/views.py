from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from todos.serializers import TodoSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuth]


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(request.data)
        # request.data["user"] = request.user
        return self.create(request, *args, **kwargs)

    def get_queryset(self):
        return self.request.user.todo_set.all().order_by('date')
    