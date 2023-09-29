from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.store.models.product import Collection


class UserLikeProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, product_id):
        user = request.user
        collection = Collection.objects.filter(id=product_id).first()
        if collection:
            if collection not in user.liked_products.all():
                user.liked_products.add(collection)
                return Response(status=status.HTTP_200_OK)
            else:
                user.liked_products.remove(collection)
                return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


__all__ = ['UserLikeProductAPIView']
