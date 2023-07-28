from rest_framework.generics import ListAPIView

from apps.store.models.product import Brand
from .serializers import BrandListSerializer


class BrandListAPIView(ListAPIView):
    serializer_class = BrandListSerializer
    queryset = Brand.objects.all()


__all__ = ['BrandListAPIView']
