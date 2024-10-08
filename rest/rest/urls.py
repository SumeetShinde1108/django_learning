from django.contrib import admin
from django.urls import path
from restapp.views import show_data,show_details,create_data
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<int:pk>',show_data),
    path('all/',show_details),    
    path('stureg/',create_data)
]

