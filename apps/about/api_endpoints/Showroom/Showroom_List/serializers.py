from rest_framework.serializers import ModelSerializer

from apps.about.models import Showroom, ShowroomDetails


class ShowroomListSerializer(ModelSerializer):
    class Meta:
        model = Showroom
        fields = ['id', 'title', 'content', 'stats', 'video', 'details']
        depth = 2


class ShowroomDetailsSerializer(ModelSerializer):
    class Meta:
        model = ShowroomDetails
        fields = '__all__'
        depth = 1
