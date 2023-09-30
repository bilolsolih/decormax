from datetime import timedelta
import os

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    'http://localhost:8080',
    'https://localhost:8080',
    'http://localhost:5173',
    'https://localhost:5173',
    'https://maxdecor.uz',
    'https://www.maxdecor.uz',
    'http://maxdecor.uz',
    'http://192.168.2.167:8080'
]
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:8080',
    "https://maxdecor.uz",
    "https://www.maxdecor.uz"
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.AllowAny",),
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ),
    # "DEFAULT_THROTTLE_RATES": {
    #     "anon": "10/second",
    #     "user": "10/second",
    # },
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.JSONParser",
    ),
    "PAGE_SIZE": 12
}

LOGIN_URL = "users:user_login"
LOGOUT_URL = "users:user_logout"

AUTH_USER_MODEL = "users.User"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST_USER = os.getenv('SMTP_USERNAME')
EMAIL_HOST_PASSWORD = os.getenv('SMTP_PASSWORD')

SWAGGER_SETTINGS = {
    'LOGIN_URL': 'users:user_login',
    'LOGOUT_URL': 'users:user_logout'
}
