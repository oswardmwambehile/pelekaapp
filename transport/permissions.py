from rest_framework import permissions

class IsOwnerTransporter(permissions.BasePermission):
    """
    Allows access only to the owner (transporter) of the TransportCompany or Vehicles under that company.
    """

    def has_object_permission(self, request, view, obj):
        if not request.user.is_authenticated or request.user.user_type != 'transporter':
            return False
        
        # If the object has 'user' attribute (TransportCompany)
        if hasattr(obj, 'user'):
            return obj.user == request.user
        
        # If the object has 'company' attribute (Vehicle)
        if hasattr(obj, 'company') and hasattr(obj.company, 'user'):
            return obj.company.user == request.user
        
        return False
