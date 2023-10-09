from rest_framework import serializers

from apps.store.models.product import Articul, Collection


class CollectionInArticulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']


class ArticulListSerializer(serializers.ModelSerializer):
    collection = CollectionInArticulSerializer(many=False)

    class Meta:
        model = Articul
        fields = ['id', 'title', 'photo', 'collection']
