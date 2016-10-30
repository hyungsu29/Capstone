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
cls=Mecab()

def TF(nouns):
	allsize=len(nouns)
	ret=dict()
	for noun in nouns:
		ret[noun]=0
	for noun in nouns:
		ret[noun]+=1
	for r in ret:
		ret[r]/=allsize
	return ret
def TFIDF(allword, tf):
	ret=tf
	for word in ret:
		idf=allword[word]
		ret[word]*=idf
		
	return ret
def calcallword(allword, nouns):
	for noun in nouns:
		allword[noun]=0

def readjson(fn):
	f=open(fn,'r')
	js=json.loads(f.read())
	f.close()
	return js

def main():
	allword=dict()
	start_time=time.time()
	DATA=readjson(FILEPATH)
	i=0
	for data in DATA:
		subject=data['subject']
		contents=data['contents']
		raw=subject+' '+contents
		nouns=cls.nouns(raw)
		calcallword(allword, nouns)
	for data in DATA:
		subject=data['subject']
		contents=data['contents']
		raw=subject+' '+contents
		nouns=cls.nouns(raw)
		dd=dict()
		for noun in nouns:
			dd[noun]=0
		for d in dd:
			allword[d]+=1
	for word in allword:
		v=math.log(len(allword)/allword[word])
		allword[word]=v
	
	for data in DATA:
		subject=data['subject']
		contents=data['contents']
		raw=subject+' '+contents
		nouns=cls.nouns(raw)
		tfidf=TFIDF(allword,TF(nouns))
		tfidf=sorted(tfidf.items(), key=operator.itemgetter(1), reverse=True)
		print (tfidf)
if __name__=="__main__":
	main()
