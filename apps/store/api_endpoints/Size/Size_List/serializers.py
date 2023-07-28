from rest_framework.serializers import ModelSerializer

from apps.store.models.product_parameters import Size


class SizeListSerializer(ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'width', 'height']
