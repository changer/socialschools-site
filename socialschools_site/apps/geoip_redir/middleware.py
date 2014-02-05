# -*- coding: utf-8 -*-

from django.utils.functional import SimpleLazyObject

def get_country_request(ip):
    import pygeoip
    gi = pygeoip.GeoIP('data/GeoIp.dat.dat')
    country = gi.country_name_by_addr(ip)
    print 'I am here'    
    if country:
        print country

class LocationMiddleWare(object):
  
     
    def process_request(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR']
        ip = request.META['REMOTE_ADDR']
        get_country_request(ip)             
        return None
