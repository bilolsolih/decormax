from rest_framework.generics import ListAPIView

from apps.about.models import Showroom
from .serializers import ShowroomListSerializer


class ShowroomListAPIView(ListAPIView):
    serializer_class = ShowroomListSerializer
    queryset = Showroom.objects.all()


__all__ = ['ShowroomListAPIView']
