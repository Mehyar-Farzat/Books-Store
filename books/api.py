from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



from .serializers import AutherListSerializer, AutherDetailSerializer, BookListSerializer, BookDetailSerializer
from .models import Auther, Book, Review

class AutherListAPI(generics.ListCreateAPIView):
    serializer_class= AutherListSerializer 
    queryset= Auther.objects.all()

class AutherDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= AutherdetailSerializer 
    queryset= Auther.objects.all()

class BookListAPI(generics.ListCreateAPIView):
    serializer_class= BookListSerializer 
    queryset= Book.objects.all()

class BookDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    serializer_class= BookDetailSerializer 
    queryset= Book.objects.all()