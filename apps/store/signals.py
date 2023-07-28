from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.store.models.product import Product, Variant
from .tasks import photo_compress


@receiver(post_save, sender=Product)
@receiver(post_save, sender=Variant)  #
def news_or_picture_saved(sender, instance, created, **kwargs):
    if created and instance.photo and instance.photo.width > 2114:
        photo_compress(instance.pk, instance._meta.app_label, instance._meta.model_name)
