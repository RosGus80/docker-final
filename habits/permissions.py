from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Дает право взаимодействовать с привычкой только ее создателю, остальным - только читать
    (для публичных привычек)"""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            if view.get_object.is_public:
                return True
        return view.get_objwct.owner == request.user
