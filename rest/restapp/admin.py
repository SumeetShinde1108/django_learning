from django.contrib import admin

from restapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']

admin.site.register(Student)
