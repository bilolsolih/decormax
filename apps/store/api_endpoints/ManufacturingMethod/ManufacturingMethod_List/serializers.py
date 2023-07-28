from rest_framework.serializers import ModelSerializer

from apps.store.models.product_parameters import ManufacturingMethod


class ManufacturingMethodListSerializer(ModelSerializer):
    class Meta:
        model = ManufacturingMethod
        fields = ['title']
