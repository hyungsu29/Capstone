import operator
import json
import os
import sys
f=open('R.csv','r')
lines=f.readlines()
f.close()
d=dict()
allword=0
_site=sys.argv[1]
_startdate=sys.argv[2]
_enddate=sys.argv[3]
ppp = open('filter_list','r')
filter_list = ppp.readline().split(' ')
ppp.close()


for line in lines:
	raw=line.split(',')
	date=raw[0].strip()
	site=raw[1].strip()
	words=raw[2].strip()
	if(_site!=site or date<_startdate or _enddate<date):
		continue
	words=raw[2].split(' ')
	for word in words:
		word=word.strip()
		if(len(word)<1):
			continue
		d[word]=0
		allword+=1

for line in lines:
	raw=line.split(',')
	date=raw[0].strip()
	site=raw[1].strip()
	words=raw[2].strip()
	if(_site!=site or date<_startdate or _enddate<date):
		continue
	words=raw[2].split(' ')
	for word in words:
		word=word.strip()
		if(len(word)<1):
			continue
		d[word]+=1
sorted_d=sorted(d.items(), key=operator.itemgetter(1), reverse=True)
idx=1
retlist=list()
for item in sorted_d:
	if item[0] in filter_list:
		continue
	if(idx==11):
		break
	v=dict()
	v['rank']=idx
	v['keyword']=item[0].strip()
	v['Frequency']=item[1]
	v['percent']=round((float(v['Frequency'])/allword)*100.0,1)
	retlist.append(v)
	idx+=1
retjson=json.dumps(retlist,ensure_ascii=False)
f=open('./examjson/gettable.json','w')
f.write(retjson)
f.close()
