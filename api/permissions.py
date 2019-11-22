from rest_framework import permissions
from .models import ApiKey


class ApiKeyPermission(permissions.BasePermission):
    def has_permission(self,  request, view):

        if request.GET.get('api_key', None) is None:
            return False
        try:
            ApiKey.objects.get(key=request.GET.get('api_key', None))
            return True
        except ApiKey.DoesNotExist:
            return False

    def has_object_permission(self, request, view, obj):
        try:
            k = ApiKey.objects.get(key=request.GET.get('api_key', None))
        except ApiKey.DoesNotExist:
            return False
        if not hasattr(obj, 'owner'):
            return True
        if getattr(obj, 'owner') == k.owner:
            return True
        return False
