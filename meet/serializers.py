from django.contrib.auth.models import User
from rest_framework import serializers

from meet.models import Room, MemberShip


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class RequestJoinRoomSerializer(serializers.ModelSerializer):
    room = serializers.SlugRelatedField(queryset=Room.objects.all(),
                                        slug_field='name')

    class Meta:
        model = MemberShip
        fields = ('room',)

    def create(self, validated_data):
        user = self.context['request'].user
        status_user = MemberShip.objects.create(user=user, **validated_data)

        return status_user


class MemberShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberShip
        fields = '__all__'

        read_only_fields = [
            'is_owner',
            'room',
            'user'
        ]


class ShowTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=200)
