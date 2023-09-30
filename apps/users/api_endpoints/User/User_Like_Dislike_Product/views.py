from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.store.models.product import Collection


class UserLikeProductAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, product_id, *args, **kwargs):
        self.like_or_dislike(request.user, product_id)

        return Response(status=status.HTTP_200_OK)

    def like_or_dislike(self, user, product_id):
        try:
            collection = Collection.objects.get(id=product_id)
            if collection not in user.liked_products.all():
                user.liked_products.add(collection)
            else:
                user.liked_products.remove(collection)
        except Collection.DoesNotExist:
            raise ValueError('No such collection.')
        except Exception as e:
            raise ValueError(e)


__all__ = ['UserLikeProductAPIView']
