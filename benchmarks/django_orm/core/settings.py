from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = (
    "django-insecure-nnmjvoy+&$&5_l3r=ibdd8y4a=1^vz+ta6#w3rcu5p+09o+_)4"
)


# Application definition
INSTALLED_APPS = [
    "app",
]

ROOT_URLCONF = "core.urls"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "perfdb",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "localhost",
        "PORT": 5432,
        "OPTIONS": {
            "pool": {
                "max_size": 10,
            },
        },
    },
}
