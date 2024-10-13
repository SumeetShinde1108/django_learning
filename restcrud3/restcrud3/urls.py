from django.contrib import admin
from django.urls import path
from restapp import views
from restapp.views import StudentList, StudentCreate, StudentRetrieve, StudentUpdate, StudentDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', StudentList.as_view()),
    path('students/create/', StudentCreate.as_view()),
    path('students/<int:pk>/', StudentRetrieve.as_view()),
    path('students/<int:pk>/update/', StudentUpdate.as_view()),
    path('students/<int:pk>/delete/', StudentDelete.as_view()),
]
