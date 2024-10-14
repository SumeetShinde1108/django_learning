from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
class StudentAPI(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentAPI2(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer