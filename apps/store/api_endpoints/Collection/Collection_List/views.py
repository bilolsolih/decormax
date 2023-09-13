import django_filters
from django_filters.rest_framework import FilterSet, DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination

from apps.store.models.product import Collection
from apps.store.models.product_parameters import TargetRoom, Style, PictureType, Color, Size
from .serializers import CollectionListSerializer


class CollectionFilterSet(FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    target_room = django_filters.ModelMultipleChoiceFilter(
        field_name='target_room__pk', queryset=TargetRoom.objects.all(), to_field_name='pk'
    )
    style = django_filters.ModelMultipleChoiceFilter(
        field_name='style__pk', queryset=Style.objects.all(), to_field_name='pk'
    )
    picture_type = django_filters.ModelMultipleChoiceFilter(
        field_name='picture_type__pk', queryset=PictureType.objects.all(), to_field_name='pk'
    )
    color = django_filters.ModelMultipleChoiceFilter(field_name='color__pk', queryset=Color.objects.all(), to_field_name='pk')
    size = django_filters.ModelMultipleChoiceFilter(field_name='size__pk', queryset=Size.objects.all(), to_field_name='pk')

    class Meta:
        model = Collection
        fields = ['status']


class CollectionListAPIView(ListAPIView):
    queryset = Collection.objects.all()
    serializer_class = CollectionListSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = CollectionFilterSet
    pagination_class = PageNumberPagination


__all__ = ['CollectionListAPIView']
