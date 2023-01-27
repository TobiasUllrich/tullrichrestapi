from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import ToDo
from .serializers import ToDoSerializer

# Create your views here.
class ToDoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todos to be viewed or edited.
    """
    queryset = ToDo.objects.all().order_by('created_at')
    serializer_class = ToDoSerializer
    permission_classes = [] #Zugriffsrechte falls gewünscht [permissions.IsAuthenticated]
