from rest_framework.serializers import ModelSerializer

from apps.about.models import Showroom


class ShowroomListSerializer(ModelSerializer):
    class Meta:
        model = Showroom
        fields = ['id', 'title', 'content', 'stats', 'video', 'details']
        depth = 1


