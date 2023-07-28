from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from apps.news.models import News


class NewsTestCase(TestCase):
    fixtures = ['fixtures/news/news', 'fixtures/news/pictures']

    @classmethod
    def setUpTestData(cls):
        cls.api_cline = APIClient()

    def test_news_list(self):
        response = self.api_cline.get(reverse("news:news_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)
        self.assertEqual(len(response.data), News.objects.count())

    def test_news_retrieve(self):
        response = self.api_cline.get(reverse("news:news_retrieve", args=['1']))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)
