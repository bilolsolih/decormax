from rest_framework import serializers

from apps.store.models.product import Collection


class CollectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'photo', 'picture_type', 'status', 'is_header', 'articuls']
        depth = 1
