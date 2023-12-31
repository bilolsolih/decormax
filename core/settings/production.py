from .base import *  # noqa

ALLOWED_HOSTS = ['bilolsolih.pythonanywhere.com', 'api.maxdecor.uz']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
        "ATOMIC": False,
    }
}

DEBUG = True

ADMINS = [("BlackHoler", "BilolMuhammadSolih@gmail.com")]
