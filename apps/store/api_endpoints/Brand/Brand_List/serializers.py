from rest_framework.serializers import ModelSerializer

from apps.store.models.product import Brand


class BrandListSerializer(ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'title']
