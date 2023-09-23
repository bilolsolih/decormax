from rest_framework.generics import ListAPIView

from apps.about.models import CompanyHistory
from .serializers import CompanyHistoryListSerializer


class CompanyHistoryListAPIView(ListAPIView):
    serializer_class = CompanyHistoryListSerializer
    queryset = CompanyHistory.objects.all()


__all__ = ['CompanyHistoryListAPIView']
