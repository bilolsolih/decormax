from rest_framework.serializers import ModelSerializer

from apps.news.models import News


class NewsListSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'subtitle', 'photo', 'is_header', 'created']
