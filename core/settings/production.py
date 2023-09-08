from .base import *  # noqa

ALLOWED_HOSTS = ['bilolsolih.pythonanywhere.com']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEBUG = False

ADMINS = [("BlackHoler", "BilolMuhammadSolih@gmail.com")]
