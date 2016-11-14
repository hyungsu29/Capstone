import operator
import json
import os
import sys
f=open('R.csv','r')
lines=f.readlines()
f.close()
_site=sys.argv[1].strip()
_keyword=sys.argv[2].strip()
_date=sys.argv[3].strip()
date2=_date
date2=date2[4:]
date2=date2[0]+date2[1]+'/'+date2[2:]
d=dict()
d['keyword']=_keyword
d['date']=date2
d['Frequency']=0
for line in lines:
	raw=line.split(',')
	date=raw[0].strip()
	site=raw[1].strip()
	if(date!=_date or site!=_site):
		continue
	words=raw[2].split(' ')
	for word in words:
		word=word.strip()
		if(len(word)<1):
			continue
		if(word!=_keyword):
			continue
		d['Frequency']+=1
retjson=json.dumps(d,ensure_ascii=False)
f=open('./examjson/getdata.json','w')
f.write(retjson)
f.close()
