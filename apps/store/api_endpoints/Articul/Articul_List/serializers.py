from rest_framework import serializers

from apps.store.models.product import Articul


class ArticulListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articul
        fields = ['id', 'title', 'photo']
