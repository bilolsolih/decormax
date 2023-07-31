from rest_framework.generics import RetrieveAPIView

from apps.news.models import News
from .serializers import NewsRetrieveSerializer


class NewsRetrieveAPIView(RetrieveAPIView):
    serializer_class = NewsRetrieveSerializer
    queryset = News.objects.all()

    def get_object(self):
        return News.objects.filter(pk=self.kwargs.get('pk')).first()


__all__ = ['NewsRetrieveAPIView']
