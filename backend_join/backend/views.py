from django.shortcuts import render
from rest_framework import viewsets
from .models import Task, Contact
from .serializers import TaskSerializer , ContactSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
