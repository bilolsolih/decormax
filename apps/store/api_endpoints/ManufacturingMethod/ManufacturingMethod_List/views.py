from rest_framework.generics import ListAPIView

from apps.store.models.product_parameters import ManufacturingMethod
from .serializers import ManufacturingMethodListSerializer


class ManufacturingMethodListAPIView(ListAPIView):
    serializer_class = ManufacturingMethodListSerializer
    queryset = ManufacturingMethod.objects.all()


__all__ = ['ManufacturingMethodListAPIView']
