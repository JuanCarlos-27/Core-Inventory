import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}

MYSQL = {
    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PSW'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT')
    }
}
POSTGRESQL = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'proyecto_core_inventory',
        'USER': 'postgres',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}