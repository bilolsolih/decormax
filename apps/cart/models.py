from django.db import models
from django.db.models.aggregates import Sum
from django.utils.translation import gettext_lazy as _


class Cart(models.Model):
    user = models.OneToOneField(
        verbose_name=_('User'), to='users.User', related_name='cart', on_delete=models.CASCADE, blank=True, null=True
    )

    @property
    def get_price(self):
        return self.items.aggregate(total=Sum('cost'))['total']

    class Meta:
        verbose_name = _('Cart')
        verbose_name_plural = _('Carts')

    def __str__(self):
        return f"{self.user.username}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(
        verbose_name=_('Cart'), to='cart.Cart', related_name='items', on_delete=models.CASCADE, blank=True, null=True
    )
    device_id = models.CharField(verbose_name=_('Device id'), max_length=64, blank=True, null=True)
    collection = models.ForeignKey(
        verbose_name=_('Collection'), to='store.Collection', on_delete=models.SET_NULL, null=True
    )
    articul = models.ForeignKey(verbose_name=_('Articul'), to='store.Articul', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'), default=0)
    cost = models.DecimalField(verbose_name=_('Cost'), max_digits=24, decimal_places=2, default=0)

    class Meta:
        verbose_name = _('Cart item')
        verbose_name_plural = _('Cart items')
        unique_together = ['cart', 'collection', 'device_id']

    def __str__(self):
        return f"{self.collection.title} - {self.quantity}pcs"
