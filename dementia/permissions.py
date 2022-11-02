from rest_framework import permissions

class AdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
        
class QuestionUserOrAdminElseReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True 
        elif obj.username == request.user:
            return True
        else:
            return bool( request.user.is_superuser)
        
        # above can be achieved using this simple code
        # else :
        #     return (bool( request.user.is_superuser) or obj.username == request.user)
         
        #if user==user 
        #  else :
        #     return obj.username == request.user
        
        
        