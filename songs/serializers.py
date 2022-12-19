from rest_framework import serializers
from users.serializers import UserSerializer

from .models import Song


# class SongSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=255)
#     duration = serializers.CharField(max_length=255)
#     album_id = serializers.IntegerField(read_only=True)

#     def create(self, validated_data):
#         return Song.objects.create(**validated_data)


class SongSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Song
        fields = '__all__'