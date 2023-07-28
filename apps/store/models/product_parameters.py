from django.db import models
from django.utils.translation import gettext_lazy as _


class TargetRoom(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Target room')
        verbose_name_plural = _('Target rooms')

    def __str__(self):
        return self.title


class Style(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Style')
        verbose_name_plural = _('Styles')

    def __str__(self):
        return self.title


class PictureType(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Picture type')
        verbose_name_plural = _('Picture types')

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)
    hexa_value = models.CharField(verbose_name=_('Hexa Value'), max_length=24)

    class Meta:
        verbose_name = _('Color')
        verbose_name_plural = _('Colors')

    def __str__(self):
        return f"{self.title} - {self.hexa_value}"


class ManufacturingMethod(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Manufacturing method')
        verbose_name_plural = _('Manufacturing methods')

    def __str__(self):
        return self.title


class Size(models.Model):
    width = models.DecimalField(verbose_name=_('Width length'), max_digits=10, decimal_places=2)
    height = models.DecimalField(verbose_name=_('Height length'), max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = _('Size')
        verbose_name_plural = _('Sizes')

    def __str__(self):
        return f"Size: {self.width} x {self.height}"


class BuildingMaterial(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=128)

    class Meta:
        verbose_name = _('Material')
        verbose_name_plural = _('Materials')

    def __str__(self):
        return self.title
