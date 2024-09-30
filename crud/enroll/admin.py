from django.contrib import admin
from enroll.models import User

@admin.register(User)
class UseraAdmin(admin.ModelAdmin):
    list_display=('id','name','email','password')

