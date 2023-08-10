from rest_framework.generics import ListAPIView

from apps.store.models.product import Articul

from .serializers import ArticulListSerializer


class ArticulListAPIView(ListAPIView):
    serializer_class = ArticulListSerializer
    queryset = Articul.objects.all()


__all__ = ['ArticulListAPIView']
