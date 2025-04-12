from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
 
        if request.method in permissions.SAFE_METHODS:
            return True
     
        return bool(request.user and request.user.is_staff)

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        
        if not request.user or not request.user.is_authenticated:
            return False

      
        if view.action == 'create':
            return request.user.is_staff or request.user.groups.filter(name='instructor').exists()

        return True

    def has_object_permission(self, request, view, obj):
        return request.user == obj.instructor or request.user.is_staff


class IsStudentOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        
        if request.user.is_staff:
            return True

       
        if request.method in permissions.SAFE_METHODS:
            return True

       
        if view.action == 'enroll' and request.method == 'POST':
            return True

        return False

    def has_object_permission(self, request, view, obj):
    
        if request.user.is_staff:
            return True
        
        elif hasattr(obj, 'instructor') and request.user == obj.instructor:
            return True
        return False

