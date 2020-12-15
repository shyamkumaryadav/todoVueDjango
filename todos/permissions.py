from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #  Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj == request.user

class IsUserAdminPost(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #  Read-only permissions are allowed for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user or request.user.is_staff
