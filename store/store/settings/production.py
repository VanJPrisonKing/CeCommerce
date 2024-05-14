from .base import *

ALLOWED_HOSTS = ['*']

# temporary, will be changed later
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}