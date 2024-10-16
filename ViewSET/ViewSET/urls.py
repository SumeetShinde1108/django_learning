from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restapp.views import StudentAPI
router = DefaultRouter()
router.register('students', StudentAPI, basename="Student")
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
    path('auth/', include('rest_framework.urls')),  
]

