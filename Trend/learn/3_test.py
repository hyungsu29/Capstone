from konlpy.tag import Twitter
from pprint import pprint
from collections import namedtuple
from gensim.models import doc2vec
import sys

avg=0
ssum=0
cntday=0
for i in range(20161101,20161128):
	cntday+=1
	sday=str(i)
	nday=str(i+1)
	doc_vectorizer=doc2vec.Doc2Vec.load('../model/'+sday+'.model')
	l=list()
	f=open('../getjson/'+sday+'.txt','r')
	lines=f.readlines()
	f.close()
	l=list()
	for line in lines:
		s=line.strip()
		print (s)
		s+='/Noun'
		try:
			doc_vectorizer.most_similar(s)
			l.append(s)
		except:
			continue
	#print (len(l))
	#print (l)
	rawresult=(doc_vectorizer.most_similar(positive=l, topn=100))
	cnt=0
	result=list()
	for r in rawresult:
		if(cnt==10):
			break
		suffix=r[0]
		suffix=suffix[len(suffix)-5:]
		#print (suffix)
		if(suffix=='/Noun'):
			cnt+=1
			result.append(r)
	print (result)
	sdict=dict()
	f=open('../getjson/'+nday+'.txt','r')
	lines=f.readlines()
	f.close()
	for line in lines:
		s=line.strip()
		s+='/Noun'
		sdict[s]=1
	score=0
	for r in result:
		pword=r[0]
		if pword in sdict:
			score+=10
	print (score)
	ssum+=score
print (cntday)
print (ssum)
avg=ssum/cntday
print (avg)
