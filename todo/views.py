from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def all_todo(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        todoserializer = TodoSerializer(todos, many= True)
        return Response(todoserializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serialize = TodoSerializer(data= request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)