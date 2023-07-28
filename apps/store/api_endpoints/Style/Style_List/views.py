from rest_framework.generics import ListAPIView

from apps.store.models.product_parameters import Style
from .serializers import StyleListSerializer


class StyleListAPIView(ListAPIView):
    serializer_class = StyleListSerializer
    queryset = Style.objects.all()


__all__ = ['StyleListAPIView']
