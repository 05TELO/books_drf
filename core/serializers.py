from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

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
        validators = [
            UniqueTogetherValidator(
                queryset=Book.objects.all(),
                fields=["title", "authors"],
                message="This book already exists",
            )
        ]
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
        validators = [
            UniqueTogetherValidator(
                queryset=Author.objects.all(),
                fields=["first_name", "last_name"],
                message="This author already exists",
            )
        ]
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
