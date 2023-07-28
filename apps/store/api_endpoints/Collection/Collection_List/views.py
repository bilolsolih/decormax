from rest_framework.generics import ListAPIView

from apps.store.models.product import Collection
from .serializers import CollectionListSerializer


class CollectionListAPIView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionListSerializer


__all__ = ['CollectionListAPIView']
