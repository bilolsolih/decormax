from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework.filterset import FilterSet
from rest_framework.generics import ListAPIView

from apps.news.models import News
from .serializers import NewsListSerializer


class NewsFilterSet(FilterSet):
    class Meta:
        model = News
        fields = ['is_header']


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NewsFilterSet


__all__ = ['NewsListAPIView']
