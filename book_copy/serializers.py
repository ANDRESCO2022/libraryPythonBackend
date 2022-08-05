from rest_framework import serializers

from .models import BookCopy


class BookCopySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BookCopy
        depth = 1
