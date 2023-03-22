from django.contrib import admin
from .models import Author, Book


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):  # noqa: F811
    pass


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    pass
