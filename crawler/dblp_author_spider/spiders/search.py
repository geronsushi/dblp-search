# -*- coding:utf-8 -*-  
from whoosh.index import create_in,open_dir
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh import index
from whoosh import  scoring
import os  
import os.path
import re
import BeautifulSoup
from lxml import html

indexRoot='/home/pami/dblp_journal_ind'
htmlRoot='/home/pami/dblp_journal'
dr = re.compile(r'<[^>]+>',re.S)

class MySchema(SchemaClass):
	path= ID(stored=True)
	title= TEXT(stored=True)
	link= TEXT
	snippest=TEXT(stored=True)
	tags= KEYWORD

def main():
	schema=Schema(title=TEXT(stored=True), path=TEXT(stored=True),content=TEXT(stored=True))
	# ix= open_dir(indexRoot)
	ix= create_in(indexRoot,schema)
	writer=ix.writer()
	count=0
	count_all=0
	for files in os.listdir(htmlRoot):

		if 'html' in files:
			cur_page=open(os.path.join(htmlRoot,files),'r').read()
			# soup=BeautifulSoup.BeautifulSoup(cur_page.decode('utf-8')) 
			# try:
				# index_body= soup.find('div',{'id':'publ-section','class':'section'}).find('ul',{'class':'publ-list'})
				# cur_page_filtered='';
				# for i in index_body:
				# 	cur_page_filtered+=dr.sub('  ',str(i))
			
			doc = html.parse(os.path.join(htmlRoot,files))
			try:
				title2 = doc.find('.//title').text
				cur_page_filtered=dr.sub(' ',cur_page)
			except:
				continue
			# titleTag=soup.html.head.title
			# print titleTag.string 
			writer.add_document(title=unicode(title2),path=unicode(os.path.join(htmlRoot,files),'utf-8'),content=unicode(cur_page_filtered,('utf-8')))
			count+=1;

			if count>50:
				count=0;
				count_all+=50
				print count_all
				writer.commit()
				ix= open_dir(indexRoot)
				writer=ix.writer()
			# except:
			# 	pass
				
				# print 'Error'
	# writer.commit()

	with ix.searcher(weighting=scoring.TF_IDF()) as searcher:
		query= QueryParser("content",ix.schema).parse(u"Behnaam Aazhang")
		results=searcher.search(query)
		# print len(results)
		for hit in results:
			print(hit["title"])
			# print hit["path"]
			# print hit.highlights("content") # This will automatically provide the highlights in th retrieved pages

if __name__=='__main__':
	main()

