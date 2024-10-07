from rest_framework import serializers
class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=45)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=45)