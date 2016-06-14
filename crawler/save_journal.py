# -*- coding: utf-8 -*-
import sys, urllib
root_path='/home/pami/dblp_journal_temp'
save_path='/home/pami/dblp_journal'
import os
import os.path
ind=0
import time
for filename in os.listdir(root_path):
	# for filename in filenames:
	try:
		if 'html' in filename:
			full_path=os.path.join(root_path,filename)
			ff=open(full_path)
			cur_url=ff.readline()
			fp=open(os.path.join(save_path,filename),'wb')
			wp = urllib.urlopen(cur_url) #打开连接
			fp.write(wp.read()) #写入数据
			fp.close()
			ff.close()
			# os.remove(full_path)
			print str(ind)+full_path
			ind+=1
			time.sleep(2)
	except :
		print 'e\n'
