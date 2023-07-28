from rest_framework.generics import ListAPIView

from apps.store.models.product_parameters import PictureType
from .serializers import PictureTypeListSerializer


class PictureTypeListAPIView(ListAPIView):
    serializer_class = PictureTypeListSerializer
    queryset = PictureType.objects.all()


__all__ = ['PictureTypeListAPIView']
