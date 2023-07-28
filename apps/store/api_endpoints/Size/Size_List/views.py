from rest_framework.generics import ListAPIView

from apps.store.models.product_parameters import Size
from .serializers import SizeListSerializer


class SizeListAPIView(ListAPIView):
    serializer_class = SizeListSerializer
    queryset = Size.objects.all()


__all__ = ['SizeListAPIView']
