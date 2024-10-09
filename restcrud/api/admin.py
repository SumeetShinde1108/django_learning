from django.contrib import admin
from api.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display=['id','name','roll','city']

admin.site.register(Student,StudentAdmin)