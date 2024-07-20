from rest_framework import serializers
from .models import Todo, user
from django.contrib.auth import get_user_model

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(read_only= True, many= True)
    class Meta:
        model = user
        fields = '__all__'