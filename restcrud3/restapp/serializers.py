from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    class meta:
        models=Student
        fields='__all__'


        def create(self,**valiadated_data):
            return Student.objects.create(**validated_data)