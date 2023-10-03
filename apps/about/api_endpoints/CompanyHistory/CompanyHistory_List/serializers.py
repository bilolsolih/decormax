from rest_framework.serializers import ModelSerializer

from apps.about.models import CompanyHistory


class CompanyHistoryListSerializer(ModelSerializer):
    class Meta:
        model = CompanyHistory
        fields = '__all__'
