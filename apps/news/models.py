import os

from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


class News(TimeStampedModel):
    title = models.CharField(verbose_name=_('Title'), max_length=256)
    subtitle = models.TextField(verbose_name=_('Subtitle'), blank=True, null=True)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='images/news/%Y/%m/%d')
    content = RichTextField(verbose_name=_('Content'))
    is_header = models.BooleanField(_('Use for header?'), default=False)

    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')
        ordering = ('-created',)

    def delete(self, *args, **kwargs):
        if self.photo.path and os.path.exists(self.photo.path):
            os.remove(self.photo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title


class Picture(TimeStampedModel):
    news = models.ForeignKey(verbose_name=_('News'), to='news.News', related_name='pictures', on_delete=models.CASCADE)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='images/news/%Y/%m/%d')

    class Meta:
        verbose_name = _('Picture')
        verbose_name_plural = _('Pictures')

    def delete(self, *args, **kwargs):
        if self.photo.path and os.path.exists(self.photo.path):
            os.remove(self.photo.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.news.title} - photo - {self.id}"
