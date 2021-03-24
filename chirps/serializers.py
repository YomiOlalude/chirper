from rest_framework import serializers
from .models import *
from django.conf import settings

MAX_CHIRP_LENGTH = settings.MAX_CHIRP_LENGTH
CHIRP_ACTION_OPTIONS = settings.CHIRP_ACTION_OPTIONS

class ChirpCreateSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Chirp
        fields = ["id", "content", "likes"]
    def get_likes(self, obj):
        return obj.likes.count() 
    
    def validate_content(self, value):
        if len(value) > MAX_CHIRP_LENGTH:
            raise serializers.ValidationError("Sorry, this Chirp is too long")
        return value
    
    
class ChirpSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField(read_only=True)
    content = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Chirp
        fields = ["id", "content", "likes"]
        
    def get_likes(self, obj):
        return obj.likes.count() 
    
    def get_content(self, obj):
        return obj.content


class ChirpActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)
    
    def validate_action(self, value):
        value = value.lower().strip()
        if not value in CHIRP_ACTION_OPTIONS:
            raise serializers.ValidationError("This is not a valid action for chirps")
        return value 
        
