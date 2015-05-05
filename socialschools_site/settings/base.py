# Django base settings for socialschools_site project.

import os
import dj_database_url

gettext = lambda s: s

PROJECT_ROOT = os.sep.join(os.path.abspath(os.path.dirname(__file__))\
                     .split(os.sep)[:-2])

APP_ROOT = os.sep.join(os.path.abspath(os.path.dirname(__file__))\
                     .split(os.sep)[:-1])

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('SocialSchools Support', 'support@socialschools.nl'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL', 'postgres://localhost/socialschools_site'))
}

# Allow all host headers (filtered by heroku router)
ALLOWED_HOSTS = ['*']


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Amsterdam'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(os.environ.get("WWW_DIR", PROJECT_ROOT), "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.environ.get("WWW_DIR", PROJECT_ROOT), "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(APP_ROOT, "static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'qp28ka7-7**(zn@#w10m3ia&yv^k*re2!lr3(6lns%2er653j*'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'htmlmin.middleware.HtmlMinifyMiddleware',
    'htmlmin.middleware.MarkRequestMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'socialschools_site.apps.geoip_redir.middleware.LocationMiddleWare',
)

ROOT_URLCONF = 'socialschools_site.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'socialschools_site.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(APP_ROOT, "templates"),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings'
)

CMS_TEMPLATES = (
    ('base.html', gettext('default')),
    ('default.html', gettext('common')),
    ('feature.html', gettext('function')),
    ('contact.html', gettext('contact')),
    ('price.html', gettext('rate')),
    ('reference.html', gettext('reference')),
    ('videos.html', gettext('videos')),
    ('vision.html', gettext('vision')),
    ('liketoshare.html', gettext('liketoshare')),
    ('extra_placeholders.html', gettext('Extra Placeholder Page')),
    ('not_campaign.html', gettext('NOT campaign Page')),
)

CMS_PLUGIN_PROCESSORS = (
    'socialschools_site.cms_plugin_processors.wrap_payoff',
)

CMS_SEO_FIELDS = True

WYM_CLASSES = ",\n".join([
    "{'name': 'btn', 'title': 'Button', 'expr': 'a'}",
    "{'name': 'btn-primary', 'title': 'Primary button', 'expr': 'a'}",
    "{'name': 'btn-large', 'title': 'Large button', 'expr': 'a'}",
])

INTERNAL_IPS = ('127.0.0.1',)


LANGUAGES = (
    ('en', gettext('English')),
    ('nl', gettext('Dutch')),
    ('cl', gettext('Chile')),
    ('in', gettext('India')),
)

CMS_LANGUAGES = {
    ## Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'nl',
            'hide_untranslated': False,
            'name': gettext('nl'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'cl',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'in',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
    ],
}


INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.redirects',


    'cms',
    'menus',
    'mptt',
    'sekizai',

    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_googlemap',
    'djangocms_snippet',
    'cmsplugin_twitter',


    'socialschools_site.apps.cmsplugin_demo',
    'socialschools_site.apps.cmsplugin_question',
    'socialschools_site.apps.cmsplugin_price',
    'socialschools_site.apps.cmsplugin_feature',
    'socialschools_site.apps.cmsplugin_testimonial',
    'socialschools_site.apps.cmsplugin_faq',
    'socialschools_site.apps.cmsplugin_shareform',
    'socialschools_site',
    'pygeoip',
    'socialschools_site.apps.geoip_redir',
    'south',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
SESSION_COOKIE_DOMAIN = 'www.socialschools.nl'
