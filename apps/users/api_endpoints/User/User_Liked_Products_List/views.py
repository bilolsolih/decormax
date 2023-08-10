from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.store.api_endpoints.Collection.Collection_List.serializers import CollectionListSerializer


class UserLikedProductsListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionListSerializer

    def get_queryset(self):
        return self.request.user.liked_products.all()
