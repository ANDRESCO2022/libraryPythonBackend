from rest_framework import viewsets

from book_copy.models import BookCopy

from .serializers import BookCopySerializer

# Create your views here.


class BookCopyViewset(viewsets.ModelViewSet):
    queryset = BookCopy.objects.all()
    serializer_class = BookCopySerializer
