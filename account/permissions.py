from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import BasePermission


class IsDriver(BasePermission):
    def has_permission(self, request, view=None):
        try:
            request.user.driver
        except (ObjectDoesNotExist, AttributeError):
            return False
        return True


class IsPassenger(BasePermission):
    def has_permission(self, request, view=None):
        try:
            request.user.passenger
        except (ObjectDoesNotExist, AttributeError):
            return False
        return True
        