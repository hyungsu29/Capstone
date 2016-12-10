from bottle import route, run, request, response
import os
import sys


@route('/getdata')
def getdata():
        # use in graph
	site=request.query.site.strip()
	keyword=request.query.keyword.strip()
	date=request.query.date.strip()
	os.system('python3 getdata.py '+site+' '+keyword+' '+date)
	f=open('./tmpfile/getdata.json','r')
	s=f.read()
	f.close()
	return s

@route('/gettable')
def gettable():
	site=request.query.site
	startdate=request.query.startdate
	enddate=request.query.enddate
	os.system('python3 gettable.py '+site+' '+startdate+' '+enddate)
	f=open('./tmpfile/gettable.json','r')
	s=f.read()
	f.close()
	return s

@route('/getpredict')
def getpredict():
	site=request.query.site.strip()
	date=request.query.date.strip()
	os.system('python3 getpredict.py '+site+' '+date)
	f=open('./tmpfile/predict_'+site+date,'r')
	s=f.read()
	f.close()
	return s

run(host='0.0.0.0', port=6974)
