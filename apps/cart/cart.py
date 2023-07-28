from decimal import Decimal
from django.conf import settings
from apps.store.models.product import Product


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product_id, quantity, price):
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': quantity, 'price': price
            }
        self.save()

    def save(self):
        self.session.modified = True
