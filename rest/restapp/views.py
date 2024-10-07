from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from restapp.models import Student
from restapp.serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer  
def show_data(request, pk):
    stu = Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')  

def show_details(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)
    return JsonResponse(serializer.data,safe=False)
        