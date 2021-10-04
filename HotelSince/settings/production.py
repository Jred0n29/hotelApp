from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'hotel',
        'USER':'postgres',
        'PASSWORD': 'jredon29',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432'
    }
}
