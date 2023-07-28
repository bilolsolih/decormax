from rest_framework.generics import ListAPIView

from apps.store.models.product_parameters import TargetRoom
from .serializers import TargetRoomListSerializer


class TargetRoomListAPIView(ListAPIView):
    serializer_class = TargetRoomListSerializer
    queryset = TargetRoom.objects.all()


__all__ = ['TargetRoomListAPIView']
