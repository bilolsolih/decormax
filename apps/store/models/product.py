import os

from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel
from apps.store.choices import PRODUCT_STATUS


class Collection(TimeStampedModel):
    title = models.CharField(verbose_name=_("Title"), max_length=128)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='images/store/collections/%Y/%m/%d')
    description = models.TextField(verbose_name=_('Description'))
    description_2 = models.TextField(verbose_name=_('Description'), blank=True, null=True)
    no_in_pack = models.PositiveIntegerField(verbose_name=_('Number in a pack'))
    status = models.CharField(verbose_name=_('Status'), choices=PRODUCT_STATUS, max_length=4, null=True, blank=True)
    brand = models.ManyToManyField(verbose_name=_('Brand'), to='store.Brand', related_name='products')
    size = models.ManyToManyField(verbose_name=_('Size'), to='store.Size', related_name='products')
    color = models.ManyToManyField(verbose_name=_('Color'), to='store.Color', related_name='products')
    target_room = models.ManyToManyField(verbose_name=_('Target room'), to='store.TargetRoom', related_name='products')
    style = models.ManyToManyField(verbose_name=_('Style'), to='store.Style', related_name='products')
    picture_type = models.ManyToManyField(verbose_name=_('Picture type'), to='store.PictureType', related_name='products')
    manufacturing_method = models.ManyToManyField(verbose_name=_('Manufacture method'), to='store.ManufacturingMethod', related_name='products')
    building_material = models.ForeignKey(verbose_name=_('Building material'), to='store.BuildingMaterial', related_name='products', on_delete=models.SET_NULL, null=True)
    price = models.PositiveIntegerField(verbose_name=_('Price'))

    active = models.BooleanField(verbose_name=_('Is active'), default=True)

    class Meta:
        verbose_name = _('Collection')
        verbose_name_plural = _('Collections')

    def delete(self, *args, **kwargs):
        if hasattr(self, 'photo') and self.photo and os.path.exists(self.photo.path):
            os.remove(self.photo.path)
        super().delete()

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')

    def __str__(self):
        return self.title


class Articul(TimeStampedModel):
    collection = models.ForeignKey(
        verbose_name=_('Collection'), to='store.Collection', related_name='articuls', on_delete=models.SET_NULL,
        null=True
    )
    title = models.CharField(verbose_name=_('Title'), max_length=256)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='images/store/articuls/%Y/%m/%d')

    class Meta:
        verbose_name = _('Articul')
        verbose_name_plural = _('Articuls')

    def delete(self, *args, **kwargs):
        if hasattr(self, 'photo') and self.photo.path and os.path.exists(self.photo.path):
            os.remove(self.photo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Video(TimeStampedModel):
    collection = models.ForeignKey(verbose_name=_('Collection'), to='store.Collection', related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(verbose_name=_('Video file'), upload_to='videos/store/articuls/%Y/%m/%d', blank=True, null=True)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='videos/store/articuls/%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name = _('Video')
        verbose_name_plural = _('Videos')

    def delete(self, *args, **kwargs):
        if hasattr(self, 'photo') and hasattr(self.photo, 'path') and self.photo.path and os.path.exists(self.photo.path):
            os.remove(self.photo.path)
        if hasattr(self, 'video') and hasattr(self.video, 'path') and self.video.path and os.path.exists(self.video.path):
            os.remove(self.video.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.collection.title}'s video - {self.pk}"
