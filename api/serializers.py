from rest_framework import serializers
class ClassRoomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name=serializers.CharField(max_length=100)
    