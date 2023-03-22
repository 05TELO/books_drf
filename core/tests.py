from rest_framework import status
from rest_framework.test import APITestCase
from .models import Author, Book


class ApiTests(APITestCase):
    def test_books(self):
        url = "/api/books/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {"title": "Fight club", "authors": []}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.get().title, "Fight club")

    def test_authors(self):
        url = "/api/authors/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = {"first_name": "Chuck", "last_name": "Palahniuk"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.get().first_name, "Chuck")
