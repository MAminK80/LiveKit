from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save


class Room(models.Model):
    name = models.CharField(max_length=50, unique=True)


class MemberShip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='status_user')
    is_owner = models.BooleanField(default=False)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    status = models.CharField(choices=(('1', 'reject'), ('2', 'pending'), ('3', 'accept')), default='2', max_length=100)

    class Meta:
        unique_together = ('user', 'room')

