from rest_framework import permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class IsAuthAndSafeOrIsAuthorOfObjectPermission(IsAuthenticatedOrReadOnly):
    """
    Разрешение, дающее доступ только аутентифицированным пользователям к
    небезопасным методам, объектное разрешение, дающее доступ к изменению
    объекта только автору при небезопасных методах.
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
