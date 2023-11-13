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
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_review')
    reviewer_name = models.CharField(max_length=30)
    content = models.TextField()
    rate = models.IntegerField()

    def __str__(self):
        return str(self.book) + ": " + str(self.content)  # to show the book name and the review content in admin page