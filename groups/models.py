from django.db import models
from django.contrib.auth.models import User

class CustomGroup(models.Model):
    members = models.ManyToManyField(User, through='Invite', through_fields=('group', 'invitee'))
    name = models.CharField(max_length=50)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

class Invite(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='senders')
    invitee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='invitees')
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE, related_name='groups')
    is_accepted = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    is_requested = models.BooleanField(default=False)

    def __str__(self):
        return "%s's invitation sent to %s for joining the group '%s'" %(self.sender.username, self.invitee.username, self.group.name)

class FakeCourse(models.Model):
    name = models.CharField(max_length=20, default='')
    group = models.ForeignKey(CustomGroup, on_delete=models.CASCADE)

    def __str__(self):
        return "Course '%s' in the group '%s'" %(self.name, self.group.name)
