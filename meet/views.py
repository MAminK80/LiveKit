from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Room, MemberShip
from .token import TokenGenerator
from . import permisions
from . import serializers
from .room_name_generator import RoomNameGenerator


class CreateRoomView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        generate_room_name = RoomNameGenerator()
        room_name = generate_room_name.generate_name()
        serializer = serializers.RoomSerializer(data={'name': room_name})

        if serializer.is_valid():
            instance = serializer.save()
            MemberShip.objects.create(user=request.user, is_owner=True, room=instance, status='3')
            return Response(data=serializer.data)

        return serializer.errors


class RequestJoinRoomView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = serializers.RequestJoinRoomSerializer

    def post(self, request):
        serializer = serializers.RequestJoinRoomSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

        return serializer.errors


class UpdateStatusView(APIView):
    permission_classes = [IsAuthenticated, permisions.IsOwnerPermission]
    serializer_class = serializers.MemberShipSerializer

    def patch(self, request, room_name, user_id):
        membership = MemberShip.objects.get(user_id=user_id, room__name=room_name)
        serializer = serializers.MemberShipSerializer(instance=membership, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)

        return serializer.errors


class EnterRoomView(APIView):
    permission_classes = [IsAuthenticated, permisions.JoinPermission]

    def post(self, request, room_name):
        room = Room.objects.get(name=room_name)

        token_generator = TokenGenerator(room.name)
        token = token_generator.create_token(request.user.id)
        token_serializer = serializers.ShowTokenSerializer(data={'token': token})
        if token_serializer.is_valid():
            return Response(data=token_serializer.data)

        return token_serializer.errors


class PendingListView(APIView):
    permission_classes = [permisions.IsOwnerPermission, IsAuthenticated]

    def get(self, request, room_name):
        pending_list = MemberShip.objects.filter(room__name=room_name, status='2')
        serializer = serializers.MemberShipSerializer(instance=pending_list, many=True)
        return Response(data=serializer.data)
