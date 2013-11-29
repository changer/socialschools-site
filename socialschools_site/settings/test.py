from .base import *
from S3 import CallingFormat

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = 'assets.socialschools-www.nl'
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN
AWS_S3_CUSTOM_DOMAIN = 'assets.socialschools-www.nl'
AWS_S3_SECURE_URLS = False
AWS_PRELOAD_METADATA = True
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

