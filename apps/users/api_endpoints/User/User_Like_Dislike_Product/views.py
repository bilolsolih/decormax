from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.store.models.product import Product


class UserLikeProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, product_id):
        user = request.user
        product = Product.objects.filter(id=product_id).first()
        if product:
            if product not in user.liked_products.all():
                user.liked_products.add(product)
                return Response(status=status.HTTP_200_OK)
            else:
                user.liked_products.remove(product)
                return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


__all__ = ['UserLikeProductAPIView']
