from rest_framework.serializers import ModelSerializer

from apps.store.models.product_parameters import Style


class StyleListSerializer(ModelSerializer):
    class Meta:
        model = Style
        fields = ['id', 'title']
