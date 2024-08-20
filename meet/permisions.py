from rest_framework.permissions import BasePermission
from .models import MemberShip


class JoinPermission(BasePermission):

    def has_permission(self, request, view):
        room_name = view.kwargs['room_name']
        status_user = MemberShip.objects.get(room__name=room_name, user=request.user)
        if status_user.status == '3':
            return True
        else:
            return False


class IsOwnerPermission(BasePermission):

    def has_permission(self, request, view):
        room_name = view.kwargs['room_name']
        membership = MemberShip.objects.get(room__name=room_name, user=request.user)

        return membership.is_owner
