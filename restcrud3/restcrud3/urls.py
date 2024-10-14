from django.contrib import admin
from django.urls import path
from restapp import views
from restapp.views import  LCStudentAPI , RUDStudentAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', LCStudentAPI.as_view()),
    path('students/<int:pk>/', RUDStudentAPI.as_view()),
]
