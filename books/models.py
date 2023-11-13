from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone




class Auther(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    biography = models.TextField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    auther = models.ForeignKey(Auther, on_delete=models.CASCADE, related_name='book_auther')
    publish_date = models.DateTimeField(default=timezone.now)
    price = models.FloatField()


    def __str__(self):
        return self.name