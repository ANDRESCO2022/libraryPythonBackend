from rest_framework import viewsets

from .models import UserLibrary
from .serializers import CreateUserSerializer, UserSerializer


# Create your views here.
class UserLibraryViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = UserLibrary.objects.all()

    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer
        else:
            return UserSerializer
