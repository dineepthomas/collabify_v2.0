from django.contrib import admin
from scripts.models import attendance
from scripts.forms import PostteamForm
# Register your models here.

admin.site.register(attendance)

class teamcreationAdmin(admin.ModelAdmin):
    form = PostteamForm
    def save_model(self, request, obj, form, change):
        obj.team_created_by = request.user.username
        obj.save()
