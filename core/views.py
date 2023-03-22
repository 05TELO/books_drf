from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    lookup_field = "slug"


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = "slug"
