from django.shortcuts import render
from django.contrib import auth
from django.shortcuts import render_to_response,redirect,render
from django.template import RequestContext
from whoosh.index import create_in,open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh import index
from whoosh import  scoring
import urllib
# Create your views here.
indexRoot='/home/pami/indexPath'
import logging
def search(request):
	if request.method =='GET':
		logger = logging.getLogger('django')
		
		# about page
		if 'changelog' in request.get_full_path():
			logger.info(request.get_full_path())
			return render_to_response('changelog_new.html',{},context_instance=RequestContext(request)) 
		
		# query the static page
		elif 'query' in request.get_full_path():
			full_path=urllib.unquote(request.get_full_path())
			target_page=full_path.split('/')
			logger.info(target_page)
			return render(request,target_page[-1])
		

		# index page	
		else:
			return render_to_response('index_new.html',{'has_result': False, 'query_result': []},context_instance=RequestContext(request)) 


	elif request.method =='POST':
		
		logger = logging.getLogger('django')
		logger.info(request.POST['q'])
		content='%s'%(request.POST['q'])
		page_start=int(request.POST['page'])
		ix= open_dir(indexRoot)
		with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
			query= QueryParser("content",ix.schema).parse(content)
			results=searcher.search_page(query,page_start,pagelen=10)
			logger.info(len(results))
			hit_pages=[]
			for hit in results:
				logger.info(hit["title"])
				logger.info(hit["path"])
				final_path='/query/'+hit["path"].split('/')[-1]
				logger.info(hit.highlights("content")) # This will automatically provide the highlights in th retrieved pages
				new_hit={'title':hit["title"],'path':final_path,'snippet':hit.highlights('content')}
				hit_pages.append(new_hit)
		return render_to_response('search.html', {'q':content,'query_result':hit_pages,'query_len':len(results),'page':page_start,'record_num_start':(page_start-1)*10+1},context_instance=RequestContext(request)) 
		# return render_to_response('index.html', {},context_instance=RequestContext(request)) 

