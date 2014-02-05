# -*- coding: utf-8 -*-

from django.utils.functional import SimpleLazyObject
import pygeoip 

def get_location(request):
    
    print request.META['REMOTE_ADDR']

class LocationMiddleWare(object):
   
    def process_request(self, request):
        if 'HTTP_X_FORWARDED_FOR' in request.META:
            request.META['REMOTE_ADDR'] = request.META['HTTP_X_FORWARDED_FOR']
        print request.META['REMOTE_ADDR']    
        return None
