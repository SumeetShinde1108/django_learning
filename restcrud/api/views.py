'''from django.shortcuts import render
import io
from .models import Student
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt 
def student_api(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id', None )
        if id is not None :
            stu = Student.objects.get(id=id)
            serializer=  StudentSerializer(stu)
            json_data=JSONRenderer.render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()
        serializer=StudentSerializer(stu , many=True)
        json_data=JSONRenderer.render(serializer.data)
        return HttpsResponse(json_data,content_type='application/json')        

    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StduentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            res={"msg":'Data Created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
    
    
    json_data=JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type="application/json")

'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def student_api(request):
    if request.method == 'GET':
        id = request.GET.get('id', None)
        if id is not None:
            try:
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({'error': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
