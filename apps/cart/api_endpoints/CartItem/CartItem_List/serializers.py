from rest_framework import serializers

from apps.cart.models import CartItem
from apps.store.models.product import Collection, Articul


class CollectionInCartItem(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'photo']


class ArticulInCartItem(serializers.ModelSerializer):
    class Meta:
        model = Articul
        fields = ['id', 'title', 'photo']


class CartItemListSerializer(serializers.ModelSerializer):
    collection = CollectionInCartItem(many=False)
    articul = ArticulInCartItem(many=False)

    class Meta:
        model = CartItem
        fields = ['id', 'collection', 'articul', 'quantity', 'cost']
