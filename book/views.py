from django.shortcuts import render
from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets


# Create your views here.
from .serializers import BookSerializer
from.models import Book
# class BookListAPiView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class=  BookSerializer
#     filter_backends = [filters.SearchFilter]
#     search_fields = ['title','topic','date_puplicate','category']

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','topic','date_puplicate','category']
