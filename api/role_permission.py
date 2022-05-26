from rest_framework import permissions

class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.role == 'ad':
            return True

        return False

class IsAmbulance(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.role == 'am':
            return True

        return False

class IsUser(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.role == 'u':
            return True

        return False

class IsHealthFacility(permissions.BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if user.role == 'h':
            return True

        return False