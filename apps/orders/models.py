from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

from .choices import DELIVERY_TYPES, ORDER_STATUS


class Order(models.Model):
    user = models.ForeignKey(verbose_name=_('User'), to='users.User', related_name='orders', on_delete=models.CASCADE, blank=True, null=True)
    store = models.ForeignKey(verbose_name=_('Store'), to='store.Store', related_name='orders', on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(verbose_name=_('Full name'), max_length=128)
    phone_number = PhoneNumberField(verbose_name=_('Phone number'), region='UZ')
    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True)
    delivery_type = models.CharField(verbose_name=_('Delivery type'), choices=DELIVERY_TYPES, max_length=1)
    payment_method = models.ForeignKey(verbose_name=_('Payment method'), to='orders.PaymentType', related_name='orders', on_delete=models.SET_NULL, null=True)
    final_price = models.DecimalField(verbose_name=_('Final price'), max_digits=24, decimal_places=2, default=0)

    city = models.CharField(_('Destination city'), max_length=128, blank=True, null=True)
    region = models.CharField(_('Region'), max_length=128, blank=True, null=True)
    address = models.CharField(_('Address'), max_length=128, blank=True, null=True)
    level = models.CharField(_('Floor number'), max_length=128, blank=True, null=True)
    delivery_date = models.DateField(_('Delivery date'), blank=True, null=True)

    created = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)

    status = models.CharField(verbose_name=_('Status'), max_length=1, choices=ORDER_STATUS, default='p')

    class Meta:
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')

    @property
    def get_collection_articuls(self):
        response = dict()
        if self.items:
            for item in self.items.all():
                response[item.id]['collection'] = item.collection.title
                response[item.id]['articul'] = item.artikul.title
        return response

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        verbose_name=_('Order'), to='orders.Order', related_name='items', on_delete=models.CASCADE
    )
    collection = models.ForeignKey(
        verbose_name=_('Collection'), to='store.Collection', related_name='orders', on_delete=models.SET_NULL, null=True
    )
    artikul = models.ForeignKey(verbose_name=_('Articul'), to='store.Articul', related_name='orders',
                                on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
    cost = models.DecimalField(verbose_name=_('Cost'), max_digits=24, decimal_places=2)

    @property
    def get_product_title(self):
        return self.collection.title

    class Meta:
        verbose_name = _('Order item')
        verbose_name_plural = _('Order items')

    def __str__(self):
        return f"{self.get_product_title} - {self.quantity} - {self.cost}"


class PaymentType(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Payment type')
        verbose_name_plural = _('Payment types')

    def __str__(self):
        return self.title

# todo: api lardagi permissionlarni ko'rib chiqish
