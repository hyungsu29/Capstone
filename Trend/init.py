import os
import json
from konlpy.tag import Mecab
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Twitter
import pymysql
import math
import time
import operator
import sys
FILEPATH="./result.json"
DATA={}
cls=list()
cls.append(Mecab())
cls.append(Komoran())
cls.append(Twitter())
maxfreq=dict()
site=sys.argv[1]
site=site.strip()
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

def readdb():
	conn = pymysql.connect(host='localhost', user='root', password='9999', db='capstone', charset='utf8')
	curs = conn.cursor(pymysql.cursors.DictCursor)
	curs.execute("select * from DB1 where site="+"'"+site+"' order by date asc")
	rows=curs.fetchall()

	data=json.dumps(rows, ensure_ascii=False)
	print(data)
	return rows


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
	DATA=readdb()
	#DATA=readjson(FILEPATH)
	i=0

	for data in DATA:
		subject=data['subject']
		print(subject)
		contents=data['contents']
		#raw=subject+' '+contents
		raw=subject
		raw=raw.strip()
		nouns=getnouns(raw)
		initallword(allword, nouns)
		initallword(maxfreq, nouns)
	for data in DATA:
		subject=data['subject']
		contents=data['contents']
		#raw=subject+' '+contents
		raw=raw.strip()
		raw=raw.strip()
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
		v=math.log(len(allword)/(allword[word]+1))
		allword[word]=v
	#print (maxfreq)
	final=allword
	for f in final:
		final[f]=0
	f=open('R.csv','w')

	for data in DATA:
		subject=data['subject']
		contents=data['contents']
		date=data['date'].replace('.','')
		#raw=subject+' '+contents
		raw=subject
		raw=raw.strip()
		nouns=getnouns(raw)
		tfidf=TFIDF(allword,TF(nouns))
		tfidf=sorted(tfidf.items(), key=operator.itemgetter(1), reverse=True)
		j=0
		for kk in tfidf:
			if(j>=20):
				break
			q=str(date)+','+kk[0]
			q=q.strip()
			f.write(q)
			f.write('\n')
			#print (kk[0])
			final[kk[0]]+=1
			j+=1
	#	print ('----------------------------------------------')
	f.close()
	final=sorted(final.items(), key=operator.itemgetter(1), reverse=True)
	#print (final)
	f=open('R.csv','r')
	q=''
	qq=''
	oridate=''
	lines=f.readlines()
	f.close()
	for line in lines:
		raws=line.split(',')
		date=raws[0].strip()
		keyword=raws[1].strip()
		if(date!=oridate):
			qq+=q
			qq+='\n'
			q=date+','+site+','
			oridate=date
		if(date==oridate):
			q+=' '
			q+=keyword
			
	if(len(q)>10):
		qq+=q
	f=open('R.csv','w')
	f.write(qq.strip())
	f.close()
		
if __name__=="__main__":
	main()
