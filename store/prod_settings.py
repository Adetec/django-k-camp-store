import os
from .settings import *
import dj_database_url

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com',]

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey' # this is exactly the value 'apikey'
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_PORT = 587
EMAIL_USE_TLS = True
