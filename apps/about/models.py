from ckeditor.fields import RichTextField
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
    house_no = models.CharField(verbose_name=_('House number'), max_length=12)

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


class CompanyHistory(models.Model):
    year = models.CharField(_('Year'), max_length=4)
    content = RichTextField(_('Content'))

    class Meta:
        verbose_name = _('Company history (About Fabric)')
        verbose_name_plural = _('Company histories (About Fabric)')

    def __str__(self):
        return f"Company history for - {self.year}"


class CompanyStat(models.Model):
    icon = models.ImageField(_('Stat icon'), upload_to='images/about/company_stats/')
    title = models.CharField(_('Stat title'), max_length=256)
    content = RichTextField(_('Content'))

    class Meta:
        verbose_name = _('Company stat')
        verbose_name_plural = _('Company stats')

    def __str__(self):
        return f"Stats for - {self.title}"


class ContactPhoneNumber(models.Model):
    title = models.CharField(max_length=256, verbose_name=_('Title'))
    phonenumbers = models.CharField(verbose_name=_('Phone Number'), null=True, blank=True, max_length=15)

    class Meta:
        verbose_name = _('Contact number for page')
        verbose_name_plural = _('Contact numbers for page')

    def __str__(self):
        return self.title


class Contact(models.Model):
    type = models.CharField(max_length=256, verbose_name=_('Type'))
    title = models.CharField(max_length=256, verbose_name=_('Title'))
    phonenumbers = models.ForeignKey(to='ContactPhoneNumber', verbose_name=_('Phone Number'), null=True, blank=True,
                                     on_delete=models.SET_NULL)
    address = RichTextField(_('Description'))
    location = models.TextField(verbose_name=_('Location for iFrame'), null=True, blank=True)
    social_media = models.ManyToManyField(to='SocialMedia', verbose_name=_('Social Media'), null=True, blank=True)

    class Meta:
        verbose_name = _('Contact page')
        verbose_name_plural = _('Contacts page')

    def __str__(self):
        return f"Shop contacts for - {self.title}"


class Showroom(models.Model):
    title = models.CharField(max_length=256, verbose_name=_('Title'))
    content = RichTextField(_('Content'))
    stats = models.ManyToManyField(to='CompanyStat', verbose_name=_('Stats'))
    video = models.FileField(verbose_name=_('Video file'), upload_to='videos/about/showroom/%Y/%m/%d', blank=True,
                             null=True)

    class Meta:
        verbose_name = _('Showroom page')
        verbose_name_plural = _('Showrooms page')

    def __str__(self):
        return f"Showroom info for - {self.title}"


class ShowroomDetails(models.Model):
    showroom = models.ForeignKey(to='Showroom', verbose_name=_('Showroom'), null=True, blank=True,
                                 on_delete=models.SET_NULL, related_name='details')
    title = models.CharField(verbose_name=_('Title'), max_length=256)
    content = models.TextField(_('Content'))
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='images/about/showroom/%Y/%m/%d')
    photo_two = models.ImageField(verbose_name=_('Photo'), upload_to='images/about/showroom/%Y/%m/%d')

    class Meta:
        verbose_name = _('Showroom Detail')
        verbose_name_plural = _('Showrooms Detail')

    def __str__(self):
        return f"Showroom info for - {self.title}"
