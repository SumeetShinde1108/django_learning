from django.contrib import admin
from django.urls import path
from restapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/<int:pk>',views.show_data),
    path('all',views.show_details),    
]
