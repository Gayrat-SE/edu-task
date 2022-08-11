from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsTeacher(BasePermission):

    def has_permission(self, request, view):
        return request.user.teacher

class IsAdminOrReadOnly(BasePermission):

    def has_permission(self, request, view):
        if request.method in list(SAFE_METHODS):
            return True

        return bool(request.user and request.user.is_staff)

class IsStudent(BasePermission):

    def has_permission(self, request, view):
        return request.user.student