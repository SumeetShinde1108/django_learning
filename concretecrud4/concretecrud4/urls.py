from django.contrib import admin
from django.urls import path
from restapp.views import StudentAPI,StudentAPI2
from restapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', views.StudentAPI.as_view()),
    path('student/<int:pk>/', views.StudentAPI2.as_view())
]
