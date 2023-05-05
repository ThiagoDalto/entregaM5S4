from rest_framework import permissions
import ipdb
from rest_framework.views import Request, View
from movies.models import Movie


class IsAuthenticated(permissions.BasePermission):
    def has_permission(
        self,
        request: Request,
        view: View,
    ) -> bool:
        return request.user.is_authenticated
