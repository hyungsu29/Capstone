from konlpy.tag import Twitter
from pprint import pprint
from collections import namedtuple
from gensim.models import doc2vec
import sys
import os
site=sys.argv[1]
site=site.strip()
getday=sys.argv[2]
getday=int(getday)
avg=0
ssum=0
cntday=0
for i in range(getday,getday+1):
	cntday+=1
	sday=str(i)
	nday=str(i+1)
	doc_vectorizer=doc2vec.Doc2Vec.load('./model/'+sday+'.model')
	l=list()
	os.system('python getjson.py '+site+' '+sday)
	f=open('./tmpfile/gettable_'+site+sday,'r')
	lines=f.readlines()
	f.close()
	l=list()
	for line in lines:
		s=line.strip()
		#print (s)
		s+='/Noun'
		try:
			doc_vectorizer.most_similar(s)
			l.append(s)
		except:
			continue
	#print (len(l))
	#print (l)
	rawresult=(doc_vectorizer.most_similar(positive=l, topn=100))
	result=list()
	cnt=0
	for r in rawresult:
		#print (r)
		if(cnt==10):
			break
		if(len(r[0])<=6):
			continue
		suffix=r[0]
		suffix=suffix[len(suffix)-5:]
		suffix=suffix.strip()
		if(suffix=='/Noun'):
			result.append(r)
			cnt+=1
#	print (result)
	ret=list()
	No=0
	print (site)
	print (sday)
	f=open('./tmpfile/predict_'+site+sday,'w')
	for r in result:
		No+=1
		d=dict()
		d['No']=No
		d['Predicted Keyword']=r[0].replace('/Noun','')
		d['Frequency']=round(r[1]*100,2)
		ret.append(d)
	print (ret)
	f.write(str(ret))
	f.close()

print ('asd')


