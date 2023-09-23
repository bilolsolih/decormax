from rest_framework.generics import ListAPIView

from apps.about.models import CompanyStat
from .serializers import CompanyStatListSerializer


class CompanyStatListAPIView(ListAPIView):
    serializer_class = CompanyStatListSerializer
    queryset = CompanyStat.objects.all()


__all__ = ['CompanyStatListAPIView']
