from rest_framework.serializers import ModelSerializer

from apps.store.models.product import Product


class ProductRetrieveSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'get_collection',
            'title',
            'photo',
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
        ]
        depth = 1
