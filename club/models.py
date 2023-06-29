from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
    name = models.CharField(max_length=100)
    detail = models.CharField(max_length=300)
    members = models.FloatField()

def __str__(self):
    return self.title
