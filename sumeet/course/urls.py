from . import views
from django.urls import path


urlpatterns=[
    path('learndj/',views.learn_django),
    path('learnpy/',views.learn_python),
    path('',views.index),
    path('learnm/',views.learn_math),
    path('lernf/',views.learn_format),
    path('learnv/',views.learn_variable)
]