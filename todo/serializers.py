from django.contrib.auth.models import User
from rest_framework import serializers
from .models import ToDo

# Serializers define the API representation.
class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = ['id', 'title', 'description', 'created_at'] #'user']