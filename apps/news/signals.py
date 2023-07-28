from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.news.models import News, Picture
from .tasks import photo_compress


@receiver(post_save, sender=Picture)
@receiver(post_save, sender=News)
def news_or_picture_saved(sender, instance, created, **kwargs):
    if created and instance.photo and instance.photo.width > 1920:
        photo_compress.delay(instance.pk, instance._meta.app_label, instance._meta.model_name)
