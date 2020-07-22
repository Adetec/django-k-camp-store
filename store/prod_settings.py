import os
from .settings import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com',]

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
