from rest_framework import serializers

from book.serializers import BookSerializer
from .models import Author


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    book = BookSerializer(read_only=True)

    class Meta:
        model = Author
        fields = '__all__'
