from django.contrib import admin

from my_profile.models import ProfileModel


# Register your models here.
@admin.register(ProfileModel)
class NoteModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'bio', 'id', 'user_id']
    list_editable = ['last_name']
