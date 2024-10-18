from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.authentication import SessionAuthentication
from .permissions import MyPermission

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()  
    serializer_class = StudentSerializer 
    authentiation_classes=[SessionAuthentication]
    permission_classes=[MyPermission]
   