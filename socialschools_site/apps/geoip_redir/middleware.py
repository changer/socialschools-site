# -*- coding: utf-8 -*-

from django.utils.functional import SimpleLazyObject
import pygeoip 

def get_location(request):
    print request.META['REMOTE_ADDR']

class LocationMiddleWare(object):
    
	def process_request(self, request):
		get_location(request)
