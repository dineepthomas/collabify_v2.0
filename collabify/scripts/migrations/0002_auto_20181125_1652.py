# Generated by Django 2.0 on 2018-11-25 16:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scripts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='allMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_members', models.CharField(choices=[('Alex', 'Alex'), ('John', 'John'), ('Peter', 'Peter'), ('Rambo', 'Rambo'), ('Jason', 'Jason'), ('Eric', 'Eric'), ('WLEE', 'Win Lee'), ('Tabusu', 'Tabusu')], max_length=5)),
            ],
        ),
        migrations.AddField(
            model_name='newteamcreation',
            name='team_created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='newteamcreation',
            name='team_member',
        ),
        migrations.AddField(
            model_name='newteamcreation',
            name='team_member',
            field=models.ManyToManyField(blank=True, to='scripts.allMembers'),
        ),
    ]
