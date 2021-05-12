from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.IsAdminUser):
    """Give permissions to read only to unauthorised user"""

    def has_permission(self, request, view):
        """Overriding the defalut has permission"""
        is_admin = super().has_permission(request, view)

        return request.method in permissions.SAFE_METHODS or is_admin


class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    """Allow User to edit only their reviews"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.review_author == request.user
