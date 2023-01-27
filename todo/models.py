from django.db import models
from datetime import date
from django.contrib.auth.models import User

class ToDo(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    created_at = models.DateField(default=date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE)   
