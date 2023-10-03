from rest_framework.serializers import ModelSerializer

from apps.about.models import CompanyStat


class CompanyStatListSerializer(ModelSerializer):
    class Meta:
        model = CompanyStat
        fields = ['id', 'title', 'content', 'icon']
