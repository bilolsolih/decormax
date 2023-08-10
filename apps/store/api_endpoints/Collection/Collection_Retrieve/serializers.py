from rest_framework import serializers

from apps.store.models.product import Collection


class CollectionRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = [
            'id',
            'title',
            'description',
            'no_in_pack',
            'status',
            'brand',
            'size',
            'color',
            'target_room',
            'style',
            'picture_type',
            'manufacturing_method',
            'building_material',
            'price',
            'variants',
            'videos',
            'articuls'
        ]
        depth = 1
