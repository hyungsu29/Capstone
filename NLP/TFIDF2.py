import json
from konlpy.tag import Mecab
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Twitter

import math
import time
import operator
FILEPATH="./data.json"
DATA={}
cls=list()
cls.append(Mecab())
cls.append(Komoran())
cls.append(Twitter())
maxfreq=dict()


def TF(nouns):
	allsize=len(nouns)
	ret=dict()
	for noun in nouns:
		if(len(noun)<2):
			continue
		ret[noun]=1
	return ret

def TFIDF(allword, tf):
	ret=tf
	for word in ret:
		idf=allword[word]
		ret[word]*=idf
		
	return ret
def initallword(allword, nouns):
	for noun in nouns:
		if(len(noun)<2):
			continue
		allword[noun]=0

def readjson(fn):
	f=open(fn,'r')
	js=json.loads(f.read())
	f.close()
	return js

def getnouns(raw):
	ret=dict()
	d=list()
	d.append(dict())
	d.append(dict())
	d.append(dict())
	for i in range(0, 3):
		nouns=cls[i].nouns(raw)
		for noun in nouns:
			d[i][noun]=1
	for i in range(0, 3):
		words=d[i]
		for word in words:
			ret[word]=0
	for i in range(0, 3):
		words=d[i]
		for word in words:
			ret[word]+=1
	ret2=list()
	for w in ret.keys():
		if(ret[w]>1):
			ret2.append(w)
	return ret2

def main():
	allword=dict()
	start_time=time.time()
	DATA=readjson(FILEPATH)
	i=0

	for data in DATA:
		subject=data['subject']
		contents=data['contents']
		raw=subject+' '+contents
		nouns=getnouns(raw)
		initallword(allword, nouns)
		initallword(maxfreq, nouns)
	for data in DATA:
		subject=data['subject']
		contents=data['contents']
		raw=subject+' '+contents
		nouns=getnouns(raw)
		dd=dict()
		for noun in nouns:
			if(len(noun))<2:
				continue
			dd[noun]=0
		for noun in nouns:
			if(len(noun))<2:
				continue
			dd[noun]+=1

		for noun in nouns:
			if(len(noun))<2:
				continue
			if(maxfreq[noun]<dd[noun]):
				maxfreq[noun]=dd[noun]
		for d in dd:
			allword[d]+=1
	for word in allword:
		v=math.log(len(allword)/allword[word])
		allword[word]=v
	print (maxfreq)
	final=allword
	for f in final:
		final[f]=0
	for data in DATA:
		subject=data['subject']
		contents=data['contents']
		raw=subject+' '+contents
		nouns=getnouns(raw)
		tfidf=TFIDF(allword,TF(nouns))
		tfidf=sorted(tfidf.items(), key=operator.itemgetter(1), reverse=True)
		j=0
		for kk in tfidf:
			if(j>=3):
				break
			print (kk[0])
			final[kk[0]]+=1
			j+=1
		print ('----------------------------------------------')
	final=sorted(final.items(), key=operator.itemgetter(1), reverse=True)
	print (final)
if __name__=="__main__":
	main()
