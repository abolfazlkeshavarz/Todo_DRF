from django.shortcuts import render
from todo.models import Todo
from django.http import HttpRequest, JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
def view_home(request):
    todos = Todo.objects.order_by('priority').all()
    context = {"todos":todos}
    return render(request, 'home/index.html', context)

def todo_json(request:HttpRequest):
    todos = list(Todo.objects.order_by('priority').all().values('title', 'is_done'))
    return JsonResponse({'todos':todos})

@api_view(['GET'])
def todo_jsons(request: Request):
    todos = list(Todo.objects.order_by('priority').all().values('title', 'is_done'))
    return Response({'todos':todos})
