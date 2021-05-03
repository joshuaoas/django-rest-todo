from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Todo
from .serializers import TodoSerializer

"""
APIView: allow us to define functions that match standard HTTP methods like:
    Ex: GET, POST, PUT, PATCH, DELETE

Viewsets: allow us to define functions that match to common API object actions like: 
    Ex: LIST, CREATE, RETRIEVE, UPDATE, etc.

Viewsets are also used to write logic to perform standard database operations and to 
interface with a database back-end. And are usually used for existing database model to manage predefined objects.

The functions you add to the APIView are different than the functions you add to the ViewSet class.
"""


class TodoList(APIView):
    def get(self, request):
        todos = Todo.objects.all()
        todo_data = TodoSerializer(todos, many=True)
        return Response(todo_data.data, status=200)

    def post(self, request):
        todo = TodoSerializer(data=request.data)
        if todo.is_valid():
            todo_item = todo.save()
            todo_item.completed = False
            todo_item.url = reverse(
                'todo_one', args=[todo_item.id], request=request)
            todo_item.save()
            return Response(todo.data, status=201)
        return Response(None, status=400)

    def delete(self, request):
        Todo.objects.all().delete()
        return Response(None, status=204)


class TodoOne(APIView):
    def get(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)
            serializer = TodoSerializer(todo)
            return Response(serializer.data, status=200)
        except Todo.DoesNotExist:
            return Response(None, status=400)

    def patch(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)
            serializer = TodoSerializer(
                data=request.data, instance=todo, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=400)
        except TodoItem.DoesNotExist:
            return Response(None, status=400)

    def delete(self, request, todo_id):
        try:
            todo = Todo.objects.get(pk=todo_id)
            todo.delete()
        except todo.objects.DoesNotExist:
            return Response(None, status=400)
        return Response(None, status=204)
