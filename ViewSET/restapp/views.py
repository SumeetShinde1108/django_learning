from django.shortcuts import render
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import Student
from rest_framework.authentication  import BasicAuthentication
from rest_framework.permissions  import IsAuthenticated 
class StudentAPI(viewsets.ViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]