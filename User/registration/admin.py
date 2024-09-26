from django.contrib import admin
from registration.models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display=['name','contact','email','password']

admin.site.register(UserData,UserDataAdmin)

