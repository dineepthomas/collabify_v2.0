from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Team(models.model):
    team_name = models.CharField(max_length = 500, unique = True)
    team_description = models.TextField(max_length = 1024)
    team_logo = models.ImageField()
    team_members = models.ManyToManyField(User, through = 'Team_Member')
    team_create_date = models.DateTimeField(default = timezone.now)
    team_create_time = models.TimeField()

class Team_Member(models.model):
    team_member_name = models.CharField(max_length = 500, unique = True)
    team_member_attendance = models.PositiveSmallIntegerField()
    team_member_contribution_percentage = models.PositiveSmallIntegerField()

class Team_Board(models.model):
    team_board_name = models.CharField(max_length = 1024, unique = True)
    team_board_description = models.CharField(max_length = 1024)
    team_board_contributors = models.ManyToManyField(User, through = 'Team_Member')
    team_board_cards = models.ForeignKey()
    team_board_completion = models.PositiveSmallIntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
