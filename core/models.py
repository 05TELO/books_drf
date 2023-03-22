from django.db import models
from django.urls import reverse
from typing import Any
from django.utils.text import slugify


class Author(models.Model):
    first_name: Any = models.CharField(max_length=30)
    last_name: Any = models.CharField(max_length=40)
    email: Any = models.EmailField(blank=True, null=True)
    slug: Any = models.SlugField(blank=True, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(
                f"{self.first_name} {self.last_name}", allow_unicode=True
            )
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name}_{self.last_name}"

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"slug": self.slug})


class Book(models.Model):
    title: Any = models.CharField(max_length=100)
    authors: Any = models.ManyToManyField(
        Author, related_name="book_list", blank=True
    )
    slug: Any = models.SlugField(blank=True, null=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})
