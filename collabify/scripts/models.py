from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone


class Team(models.Model):
    team_name = models.CharField(max_length = 500, unique = True)
    team_description = models.TextField(max_length = 1024)
    team_logo = models.ImageField()
    # team_members = models.ManyToManyField(User, through = 'Team_Member')
    team_create_date = models.DateTimeField(default = timezone.now)
    team_create_time = models.TimeField()

class Team_Member(models.Model):
    team_member_name = models.CharField(max_length = 500, unique = True)
    team_member_attendance = models.PositiveSmallIntegerField()
    team_member_contribution_percentage = models.PositiveSmallIntegerField()

class Team_Board(models.Model):
    team_board_name = models.CharField(max_length = 1024, unique = True)
    team_board_description = models.CharField(max_length = 1024)
    # team_board_contributors = models.ManyToManyField(User, through = 'Team_Member')
    # team_board_cards = models.ForeignKey()
    team_board_completion = models.PositiveSmallIntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)

class allMembers(models.Model):
    team_members = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.team_members

class newTeamcreation(models.Model):
    team_name = models.CharField(max_length=100)
    team_description = models.TextField(max_length=300)
    team_member = models.ManyToManyField(User)
    dateofcreation = models.DateTimeField(default = timezone.now)
    team_created_by = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return u'%s %s %s %s' % (self.team_name, self.team_description,self.team_member,self.team_created_by)



class attendance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    attendance = models.PositiveSmallIntegerField()
    code = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    att_date = models.DateTimeField('date published')


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
