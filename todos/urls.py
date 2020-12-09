from django.urls import path, include
from rest_framework import routers
from todos import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, 'user')
router.register('todos', views.TodoViewSet, 'todo')

urlpatterns = [
    path('', include(router.urls)),
]