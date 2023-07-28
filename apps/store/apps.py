from django.apps import AppConfig


class StoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.store"

    def ready(self):
        import apps.store.signals  # noqa
        from .models import product, product_parameters, store  # noqa
