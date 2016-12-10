import urllib2
import json
import sys
import os

day=sys.argv[2]
day=str(day)
day=day.strip()

site=sys.argv[1]
site=site.strip()

os.system('python3 gettable.py '+site+' '+day+' '+day)
f=open('./tmpfile/gettable.json','r')
s=f.read()
f.close()
data=json.loads(s)
ret=''
f=open('./tmpfile/gettable_'+site+day,'w')

for i in range(1,11):
	for d in data:
		rank=d['rank']
		if(rank!=i):
			continue
		print (rank)
		s=(d['keyword'].encode('utf-8')).strip()
		#print (d['rank'])
		ret+=s
		ret+='\n'
ret=ret.strip()
print (ret)
f.write(ret)
f.close()
