import imp
from django.db import models
from django.contrib.auth.models import User


class Todo(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=False, null=True)
