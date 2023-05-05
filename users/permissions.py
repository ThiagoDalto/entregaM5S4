from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.views import Request, View
from users.models import User
import ipdb


class IsEmployee(BasePermission):
    def has_permission(self, request: Request, view: View):
        if request.method in SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_employee:
            return True
        return False


class IsAuthenticatedUser(BasePermission):
    def has_permission(self, request, view):

        return request.user.is_authenticated
