from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
# Create your views here.
@api_view(['GET', 'POST'])
def all_todos(request: Request):
    if request.method == 'GET':
        todos = Todo.objects.order_by('priority').all()
        todoserializer = TodoSerializer(todos, many = True)
        return Response(todoserializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serialize = TodoSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_201_CREATED)
    return Response(None, status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def detailed_view(request : Request, todo_id:int):
    try:
        todo = Todo.objects.get(pk=todo_id)
    except TOdo.DoesNotExist:
        return Response(None, status.HTTP_404_NOT_FOUND)



    if request.method == 'GET':
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        todo.delete()
        return Response(None, status = status.HTTP_204_NO_CONTENT)


class ListAPIView(APIView):
    def get(self, request: Request):
        todos = Todo.objects.order_by('priority').all()
        todoserializer = TodoSerializer(todos, many = True)
        return Response(todoserializer.data, status.HTTP_200_OK)
    def post(self, request: Request):
        serialize = TodoSerializer(data = request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data, status.HTTP_201_CREATED)
        return Response(None, status.HTTP_400_BAD_REQUEST)


class DetailedListAPIView(APIView):
    def get_object(self, todo_id:int):
        try:
            todo = Todo.objects.get(pk=todo_id)
            return todo
        except Todo.DoesNotExist:
            return Response(None, status.HTTP_404_NOT_FOUND)

    def get(self, request:Request, todo_id:int):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request:Request, todo_id:int):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_202_ACCEPTED)
        return Response(None, status.HTTP_400_BAD_REQUEST)        

    def delete(self, request:Request, todo_id:int):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(None, status = status.HTTP_204_NO_CONTENT)