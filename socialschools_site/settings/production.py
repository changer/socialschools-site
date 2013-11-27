import os
import urlparse

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'assets.socialschools-www.nl'
MEDIA_URL = 'http://assets.socialschools-www.nl.s3-website-eu-west-1.amazonaws.com/'

EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']

