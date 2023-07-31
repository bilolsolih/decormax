import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel
from apps.store.choices import PRODUCT_STATUS


class Collection(TimeStampedModel):
    title = models.CharField(verbose_name=_("Title"), max_length=128)

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.title


class Product(TimeStampedModel):
    collection = models.ForeignKey(
        verbose_name=_('Collection'), to='store.Collection', related_name='products', on_delete=models.SET_NULL, null=True
    )
    title = models.CharField(verbose_name=_('Title'), max_length=256)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='images/store/products/%Y/%m/%d')
    description = models.TextField(verbose_name=_('Description'))
    no_in_pack = models.PositiveIntegerField(verbose_name=_('Number in a pack'))
    status = models.CharField(verbose_name=_('Status'), choices=PRODUCT_STATUS, max_length=4, null=True, blank=True)
    brand = models.ManyToManyField(verbose_name=_('Brand'), to='store.Brand', related_name='products')
    size = models.ManyToManyField(verbose_name=_('Size'), to='store.Size', related_name='products')
    color = models.ManyToManyField(verbose_name=_('Color'), to='store.Color', related_name='products')
    target_room = models.ManyToManyField(verbose_name=_('Target room'), to='store.TargetRoom', related_name='products')
    style = models.ManyToManyField(verbose_name=_('Style'), to='store.Style', related_name='products')
    picture_type = models.ManyToManyField(verbose_name=_('Picture type'), to='store.PictureType', related_name='products')
    manufacturing_method = models.ManyToManyField(
        verbose_name=_('Manufacture method'), to='store.ManufacturingMethod', related_name='products'
    )
    building_material = models.ForeignKey(
        verbose_name=_('Building material'), to='store.BuildingMaterial', related_name='products', on_delete=models.SET_NULL, null=True
    )
    price = models.PositiveIntegerField(verbose_name=_('Price'))

    active = models.BooleanField(verbose_name=_('Is active'), default=True)

    @property
    def get_collection(self):
        return self.collection.title

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def delete(self, *args, **kwargs):
        if self.photo.path and os.path.exists(self.photo.path):
            os.remove(self.photo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Variant(TimeStampedModel):
    product = models.ForeignKey(verbose_name=_('Product'), to='store.Product', related_name='variants', on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=256)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='images/store/products/%Y/%m/%d')

    class Meta:
        verbose_name = _('Variant')
        verbose_name_plural = _('Variants')

    def delete(self, *args, **kwargs):
        if self.photo.path and os.path.exists(self.photo.path):
            os.remove(self.photo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Video(TimeStampedModel):
    product = models.ForeignKey(verbose_name=_('Product'), to='store.Product', related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(verbose_name=_('Video file'), upload_to='videos/store/products/%Y/%m/%d')
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='videos/store/products/%Y/%m/%d')

    class Meta:
        verbose_name = _('Product video')
        verbose_name_plural = _('Product videos')

    def delete(self, *args, **kwargs):
        if self.photo.path and os.path.exists(self.photo.path):
            os.remove(self.photo.path)
        if self.video.path and os.path.exists(self.video.path):
            os.remove(self.video.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.product.title}'s video - {self.pk}"

# TODO: kerakli modellarning barchasi adminga qo'shilganini tekshirish
