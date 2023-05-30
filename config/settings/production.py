from .base import *


ROOT_URLCONF = 'config.urls'
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# Security
DEBUG = False
ALLOWED_HOSTS=['https://stock-trading.up.railway.app', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://stock-trading.up.railway.app']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get("DATABASENAME"),
        'HOST':os.environ.get('MONGOHOST'),
        'USER': os.environ.get('MONGOUSER'),
        'PASSWORD': os.environ.get('MONGOPASSWORD'),
        'PORT': os.environ.get('MONGOPORT'),
        'OPTIONS': {
            'CLIENT': os.environ.get('MONGO_URL'),
            'ssl': True,
            'conn_max_age':1800
        }
    }
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
    },

    "handlers": {
        'my_log_handler': {
            'level': 'DEBUG' if DEBUG else 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {"level": "INFO", "handlers": ['my_log_handler', "console"]},
    'loggers': {
        'django': {
            'handlers': ['my_log_handler', 'console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
            'propagate': True,
        },
    },
}

# default static file renderer
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'