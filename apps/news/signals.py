from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.news.models import News, Picture
from apps.common.tasks import photo_compress


@receiver(post_save, sender=Picture)
@receiver(post_save, sender=News)
def news_or_picture_saved(sender, instance, created, **kwargs):
    if created and instance.photo and instance.photo.width > 2114:
        photo_compress(instance.pk, instance._meta.app_label, instance._meta.model_name)
# TODO: In prod, compress must be called with delay