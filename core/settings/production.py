from .base import *  # noqa
from os import getenv

ALLOWED_HOSTS = ['bilolsolih.pythonanywhere.com', 'api.maxdecor.uz']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "ATOMIC": False,
    }
}

DEBUG = False

ADMINS = [("BlackHoler", "BilolMuhammadSolih@gmail.com")]
