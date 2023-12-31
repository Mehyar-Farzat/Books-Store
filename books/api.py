from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from .serializers import AutherListSerializer, AutherDetailSerializer, BookListSerializer, BookDetailSerializer
from .models import Auther, Book, Review
from .mypagination import MyPagination
from .myfilters import BookFilter



class AutherListAPI(generics.ListAPIView):
    serializer_class= AutherListSerializer 
    queryset= Auther.objects.all()
    pagination_class = MyPagination

    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['name']
    filterset_fields=['name','age','biography']
    ordering_fields = ['age']
   
class AutherDetailAPI(generics.RetrieveAPIView):
    serializer_class= AutherDetailSerializer 
    queryset= Auther.objects.all()
    

class BookListAPI(generics.ListAPIView):
    serializer_class= BookListSerializer 
    queryset= Book.objects.all()
    
    filter_backends = [filters.SearchFilter,DjangoFilterBackend,filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['price']
    filterset_class = BookFilter

class BookDetailAPI(generics.RetrieveAPIView):
    serializer_class= BookDetailSerializer 
    queryset= Book.objects.all()