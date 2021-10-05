from .base import *

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DEBUG = False

ALLOWED_HOSTS = ['hotelsanluis.herokuapp.com']


DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6eplu40cdb5h7',
        'USER':'pxmplfkbafeywi',
        'PASSWORD': '6015cf419eb3aa0fae95f75283fd4e0c18189eb16b17de395e5822aa1f28c869',
        'HOST': 'ec2-3-209-65-193.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

STATICFILES_DIRS = (BASE_DIR,'static')