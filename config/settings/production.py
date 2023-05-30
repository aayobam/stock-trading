from .base import *
from pymongo import MongoClient

# Security
DEBUG = False
ALLOWED_HOSTS=['https://stock-trading.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://stock-trading.up.railway.app']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        #'CLIENT': MongoClient(os.environ.get('MONGO_URL'),),
        'NAME': os.environ.get("DATABASENAME"),
        'HOST':os.environ.get('MONGOHOST'),
        'USER': os.environ.get('MONGOUSER'),
        'PASSWORD': os.environ.get('MONGOUSER'),
        'PORT': os.environ.get('MONGOPORT'),
        'OPTIONS': {
            'CLIENT': os.environ.get('MONGO_URL'),
            'ssl': True,
            'conn_max_age':1800
        }
    }
}