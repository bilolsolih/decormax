from rest_framework.serializers import ModelSerializer

from apps.store.models.product_parameters import PictureType


class PictureTypeListSerializer(ModelSerializer):
    class Meta:
        model = PictureType
        fields = ['id', 'title']
