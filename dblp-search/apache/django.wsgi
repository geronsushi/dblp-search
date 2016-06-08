import os
import sys
path = '/home/pami/dblp_search'
if path not in sys.path:
	sys.path.insert(0, '/home/pami/dblp_search') 
	os.environ['DJANGO_SETTINGS_MODULE'] = ' dblp_search.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
