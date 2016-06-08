from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render_to_response
from django.template import RequestContext
# Create your views here.

def dblp(request):
	if request.method =='GET':
		        return render_to_response('index.html', 
                                  {
                                   },
                                  context_instance=RequestContext(request)) 
		   
