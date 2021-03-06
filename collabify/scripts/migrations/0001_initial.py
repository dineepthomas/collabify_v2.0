# Generated by Django 2.0 on 2018-11-24 02:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.PositiveSmallIntegerField()),
                ('code', models.CharField(max_length=100)),
                ('ip_address', models.GenericIPAddressField()),
                ('att_date', models.DateTimeField(verbose_name='date published')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='newTeamcreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('team_description', models.TextField(max_length=300)),
                ('team_member', models.CharField(choices=[('Alex', 'Alex'), ('John', 'John'), ('Peter', 'Peter'), ('Rambo', 'Rambo'), ('Jason', 'Jason'), ('Eric', 'Eric'), ('WLEE', 'Win Lee'), ('Tabusu', 'Tabusu')], max_length=5)),
                ('dateofcreation', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=500, unique=True)),
                ('team_description', models.TextField(max_length=1024)),
                ('team_logo', models.ImageField(upload_to='')),
                ('team_create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('team_create_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team_Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_board_name', models.CharField(max_length=1024, unique=True)),
                ('team_board_description', models.CharField(max_length=1024)),
                ('team_board_completion', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Team_Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_member_name', models.CharField(max_length=500, unique=True)),
                ('team_member_attendance', models.PositiveSmallIntegerField()),
                ('team_member_contribution_percentage', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
