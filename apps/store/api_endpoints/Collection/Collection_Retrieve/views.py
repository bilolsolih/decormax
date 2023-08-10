from rest_framework.generics import RetrieveAPIView

from apps.store.models.product import Collection
from .serializers import CollectionRetrieveSerializer


class CollectionRetrieveAPIView(RetrieveAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionRetrieveSerializer


__all__ = ['CollectionRetrieveAPIView']
