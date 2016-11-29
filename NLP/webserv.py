from bottle import route, run, request, response

@route('/gettable')
def gettable():
	site=request.query.site
	startdate=request.query.startdate
	enddate=request.query.enddate
	f=open('./examjson/gettable.json','r')
	s=f.read()
	f.close()
	return s

@route('/getdata')
def getdata():
	# use in graph
	site=request.query.site
	keyword=request.query.keyword
	date=request.query.date
	f=open('./examjson/getdata.json','r')
	s=f.read()
	f.close()
	return s

@route('/getpredict')
def getpredict():	
        site=request.query.site
        startdate=request.query.startdate
        enddate=request.query.enddate

        f=open('./examjson/getpredict.json','r')
        s=f.read()
        f.close()
        return s



run(host='0.0.0.0', port=6974)
