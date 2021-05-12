from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """Give permissions to read only to unauthorised user"""

    def has_permission(self, request, view):
        """Overriding the defalut has permission"""
        is_admin = super().has_permission(request, view)

        return request.method in permissions.SAFE_METHODS or is_admin
