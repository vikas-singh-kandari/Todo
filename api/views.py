from django.shortcuts import render
from .models import Todo
from .serializer import TodoSerializer
from rest_framework import viewsets

class Todoapi(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    