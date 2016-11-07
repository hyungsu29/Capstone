import json
from konlpy.tag import Mecab
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Twitter

import math
import time
import operator
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
	ret=list()
	words=raw.split(' ')
	for word in words:
		ret.append(word.strip())
	return ret


def main():
	allword=dict()
	start_time=time.time()
	f=open('R.csv','r')
	DATA=f.readlines()
	f.close()
	i=0

	for data in DATA:
		raw=data.split(',')[1]
		nouns=getnouns(raw)
		initallword(allword, nouns)
		initallword(maxfreq, nouns)
	for data in DATA:
		raw=data.split(',')[1]
		nouns=getnouns(raw)
		print(nouns)
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
	f=open('R2.csv','w')

	for data in DATA:
		date=data.split(',')[0]
		raw=data.split(',')[1]
		nouns=getnouns(raw)
		tfidf=TFIDF(allword,TF(nouns))
		tfidf=sorted(tfidf.items(), key=operator.itemgetter(1), reverse=True)
		j=0
		for kk in tfidf:
			if(j>=5):
				break
			q=str(date)+','+kk[0]
			q=q.strip()
			f.write(q)
			f.write('\n')
			print (kk[0])
			final[kk[0]]+=1
			j+=1
		print ('----------------------------------------------')
	f.close()
	f=open('R2.csv','r')
	dd=dict()
	lines=f.readlines()
	f.close()
	for line in lines:
		dd[line.strip()]=0
	f=open('R2.csv','w')
	f.write('date,keyword\n')
	dd=sorted(dd.items(),key=operator.itemgetter(0))
	for d in dd:
		s=d[0]
		f.write(s)
		f.write('\n')
	f.close()
	final=sorted(final.items(), key=operator.itemgetter(1), reverse=True)
	print (final)
	
if __name__=="__main__":
	main()
