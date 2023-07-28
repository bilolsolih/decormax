from rest_framework.generics import ListAPIView

from apps.news.models import News
from .serializers import NewsListSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


__all__ = ['NewsListAPIView']
