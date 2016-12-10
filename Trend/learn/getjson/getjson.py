import urllib2
import json


for day in range(20161101, 20161129):

	url='http://haewon.gonetis.com:6974/gettable?site=DCinside.com&startdate='+str(day)+'&enddate='+str(day)
	req=urllib2.Request(url)
	res=urllib2.urlopen(req)
	s=res.read()
	data=json.loads(s)
	f=open(str(day)+'.txt','w')
	for d in data:
		s=(d['keyword'].encode('utf-8')).strip()
		f.write(s)
		f.write('\n')


	f.close()
