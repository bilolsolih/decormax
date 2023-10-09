from rest_framework.generics import ListAPIView

from apps.store.models.product import Articul
from .serializers import ArticulListSerializer


class ArticulListAPIView(ListAPIView):
    serializer_class = ArticulListSerializer

    def get_queryset(self):
        queryset = Articul.objects.all()
        s = self.request.query_params.get('s', None)
        if s:
            queryset = queryset.filter(title__icontains=s)
        return queryset


__all__ = ['ArticulListAPIView']
