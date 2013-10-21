from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^changer5/', include(admin.site.urls)),
    url(r'^', include('cms.urls')),
)