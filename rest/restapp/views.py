import io
from django.http import JsonResponse
from django.shortcuts import render 
from restapp.models import Student
from restapp.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer 
from rest_framework.parsers import JSONParser 
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
@csrf_exempt
def show_data(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')  

def show_details(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data,safe=False)

def create_data(request):
    json_data=request.body
    stream=io.BytesIO(json_data)  
    python_data=JSONParser().parse(stream)
    serializer=StudentSerializer(python_data)
    if serializer.is_valid():
        serialiser.save()
        res={"msg":"Data created successfully!"}
        json_data=JSONRenderer().render(res) 
        return HttpResponse(json_data,content_type='application/json')
    json_data=JSONRenderer().render(serializer.errors) 
    return HttpResponse(json_data,content_type='application/json')    