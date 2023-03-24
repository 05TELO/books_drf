from rest_framework import serializers
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Author.objects.all()
    )

    class Meta:
        model = Book
        fields = (
            "title",
            "slug",
            "authors",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}


class AuthorSerializer(serializers.ModelSerializer):
    book_list = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = (
            "first_name",
            "last_name",
            "email",
            "slug",
            "book_list",
        )
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
