from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class PhoneNumber(models.Model):
    phone_number = PhoneNumberField(verbose_name=_('Phone number'), unique=True)

    class Meta:
        verbose_name = _('Phone number')
        verbose_name_plural = _('Phone numbers')

    def __str__(self):
        return self.phone_number.__str__()


class Email(models.Model):
    email = models.EmailField(verbose_name=_('Email'), unique=True)

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')

    def __str__(self):
        return self.email


class Address(models.Model):
    region = models.CharField(verbose_name=_('Region'), max_length=128)
    district = models.CharField(verbose_name=_('District'), max_length=128)
    street = models.CharField(verbose_name=_('Street'), max_length=128)
    house_no = models.CharField(verbose_name=_('House number'), max_length=3)

    class Meta:
        verbose_name = _('Address')
        verbose_name_plural = _('Addresses')

    def __str__(self):
        return f"{self.region}, {self.district}, {self.street}, {self.house_no}"


class SocialMedia(models.Model):
    social_media = models.CharField(verbose_name=_('Social Media'), max_length=128)
    link = models.URLField(verbose_name=_('Link'))

    class Meta:
        verbose_name = _('Social Media')
        verbose_name_plural = _('Social Medias')

    def __str__(self):
        return f"{self.social_media} - {self.link}"
