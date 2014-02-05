# -*- coding: utf-8 -*-

from django.utils.functional import SimpleLazyObject
from django.conf import settings

def get_country_request(ip):
    import pygeoip
    file_path = settings.PROJECT_ROOT + '/data/GeoIP.dat.dat'
    gi = pygeoip.GeoIP(file_path)
    country = gi.country_name_by_addr(ip)
    print 'I am here'    
    if country:
        return country

class LocationMiddleWare(object):
  
     
    def process_request(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR']
        ip = request.META['REMOTE_ADDR']
        country = get_country_request(ip)             
        if country == "India"
            return HttpResponseRedirect("http://socialschools-www-testing.herokuapp.com/en/")
        if country == "Netherlands":
            return HttpResponseRedirect("http://socialschools-www-testing.herokuapp.com/nl/")
        return None
