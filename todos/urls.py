from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views
from todos import views



router = routers.DefaultRouter()
router.APIRootView.__doc__ = """
This is test code `test`


`print("Hello world")`  
`from emanagement import views`
"""
router.register('todos', views.TodoViewSet, 'todo')
router.register('user', views.UserViewSet)
router.register('post', views.UserPostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', jwt_views.token_obtain_pair, name="jwt-auth"),
    path('auth/refresh/', jwt_views.token_refresh, name="jwt-auth-refresh"),
    path('auth/verify/', jwt_views.token_verify, name="jwt-auth-verify"),
]