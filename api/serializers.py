from rest_framework import serializers
from crud.models import Student, ClassRoom
class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    address = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    
class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id","name","age","address","email"]
    