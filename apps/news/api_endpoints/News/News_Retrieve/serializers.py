from rest_framework import serializers

from apps.news.models import News


class NewsRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'subtitle', 'photo', 'content', 'pictures', 'created']
        depth = 1
