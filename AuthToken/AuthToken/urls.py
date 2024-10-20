from django.contrib import admin
from rest_framework.routers import DefaultRouter
from authapp.views import ItemViewSet
from django.urls import path,include
from authapp import views
from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
router.register('students',views.ItemViewSet)
urlpatterns=[
    path('admin/',admin.site.register),
    path('',include(router.urls)),
    path('',include('rest_framework.urls')),
    path('gettoken/',obtain_auth_token)
]