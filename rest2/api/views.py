from django.shortcuts import render
from .models import Student
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import StudentSerializer 
from rest_framework import status
@api_view(['GET','POST','PUT','DELETE'])
def student_list(request):
    if request.method=="GET":
        id =request.data.get('id')
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu , many=True)
        return Response(serializer.data)     
    
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method=="PUT":
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
  
@api_view(['DELETE'])
def delete_student(request,id):
    student=Student.objects.get(pk=id)
    student.delete()
    return Response({"msg":"Data deleted successfully!"})


