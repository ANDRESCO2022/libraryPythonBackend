from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets

from .models import Book

# Create your views here.
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = {
        "title": ["contains"],
        "topic": ["contains"],
        "status": ["contains"],
        "category__id": ["contains"],
        "author__id": ["contains"],
        "date_puplicate": ["contains"],
    }
