from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Store(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)
    photo = models.ImageField(_('Store photo'), upload_to='images/store/stores/')
    info = models.TextField(_('Info about the store'), blank=True, null=True)
    phone_number = PhoneNumberField(verbose_name=_('Phone number'), region='UZ')
    region = models.CharField(verbose_name=_('Region'), max_length=128)
    district = models.CharField(verbose_name=_('City or district'), max_length=128)
    address = models.CharField(verbose_name=_('Address'), max_length=256)
    address_link = models.CharField(verbose_name=_('Address link'), max_length=256)
    working_hours = RichTextField(verbose_name=_('Working hours'))
    orient = models.CharField(verbose_name=_('Orient'), max_length=256, blank=True, null=True)
    location = models.TextField(verbose_name=_('Location for iFrame'), blank=True, null=True)

    is_certified = models.BooleanField(_('Is certified'), default=True)

    class Meta:
        verbose_name = _('Store page')
        verbose_name_plural = _('Stores page')

    def __str__(self):
        return f"{self.title} in {self.region}, {self.district}"
