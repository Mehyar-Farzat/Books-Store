from django_filters import rest_framework as filters
from .models import Book
import django_filters

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title' :['contains'],
            'price' : ['range'],
            'auther' : ['exact'],
            'publish_date':['exact']
        }