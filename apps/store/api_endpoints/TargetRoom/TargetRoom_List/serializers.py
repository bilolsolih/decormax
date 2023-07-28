from rest_framework.serializers import ModelSerializer

from apps.store.models.product_parameters import TargetRoom


class TargetRoomListSerializer(ModelSerializer):
    class Meta:
        model = TargetRoom
        fields = ['id', 'title']
