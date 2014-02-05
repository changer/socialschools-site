# -*- coding: utf-8 -*-
import pygeoip
from django.utils.functional import SimpleLazyObject
from django.conf import settings
from django.http import HttpResponsePermanentRedirect

def get_country_request(ip):
    
    file_path = settings.PROJECT_ROOT + '/data/GeoIP.dat.dat'
    gi = pygeoip.GeoIP(file_path)
    country = gi.country_name_by_addr(ip)   
    return country

class LocationMiddleWare(object):
       
    def process_request(self, request):
    # NOTICE: This will make sure redirect loop is broken.
        if request.path in ["/en/", "/nl/"]:
            return None
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR']
        ip = request.META['REMOTE_ADDR']
        country = get_country_request(ip)             
        if country == "India":
            return HttpResponsePermanentRedirect('/en/')       
        if country == "Netherlands":
            return HttpResponsePermanentRedirect('/nl/')
        return None

