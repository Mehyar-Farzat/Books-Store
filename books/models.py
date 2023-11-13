from django.db import models
from django.contrib.auth.models import User




class Auther(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    biography = models.TextField()

    def __str__(self):
        return self.name