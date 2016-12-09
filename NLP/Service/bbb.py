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
is_filter = dict()
retlist=list()


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
	f=open('R2.csv','w')
	ii=1000
	prev = 0
	cnt = 0
	filter_list = ''
	fq = dict()
	aaaaa = list()
	prev = list()
	prev_filter = prev 
	for data in DATA:
		ii-=1
		date=data.split(',')[0]
		site=data.split(',')[1]
		raw=data.split(',')[2]
		raw=raw.strip()
		nouns=getnouns(raw)
		D=dict()
		for noun in nouns:
			D[noun]=0
		for noun in nouns:
			D[noun]+=1
		#print(D)
		tfidf=sorted(D.items(), key=operator.itemgetter(1),reverse=True)

#		print(tfidf)
		j=0
		ws=date+','
		ss=''
		for qqqq in is_filter:
			is_filter[qqqq] = 0
		for kk in tfidf:
			if(j>=10):
				break
			if kk[0] in aaaaa:
				continue
			if kk[0] in prev_filter:
				if(kk[0] in fq):
					if(fq[kk[0]] > 60):
						if kk[0] not in aaaaa:
							aaaaa.append(kk[0])
						continue
				elif(kk[0] not in fq):
					fq[kk[0]]=0
				fq[kk[0]] += 1
			else:
				if kk[0] in fq:
					fq[kk[0]] = 0
			ss+=kk[0]
			print(kk[0])
			prev.append(kk[0])
			ss+=','
			j+=1
		print ('----------------------------------------------')
		if(j<0):
			continue
		ss=ss[:len(ss)-1]
		ws+=str(j)
		ws+=','
		ws+=ss
		ws+='\n'
		f.write(ws)
	fl = open('filter_list','w')
	for l in aaaaa:
		filter_list = filter_list + l + ' '
#		print('%s : %d' % (l, fq[l]))
			
	fl.write(filter_list)
	fl.close()
	f.close()
	f=open('R2.csv','r')
	lines=f.readlines()
	f.close()
	f=open('R2.csv','w')
	ws=''
	for i in range(0, len(lines)):
		idx=len(lines)-1-i
		ws+=lines[idx].strip()
		ws+='\n'
	f.write(ws.strip())
	f.close()
	seqnum=1
	ii=0
	f=open('R2.csv','r')
	lines=f.readlines()
	f.close()
	ws=''
	for line in lines:
		line=line.strip()
		ii+=1
		if(ii==1 or ii==len(lines)):
			ws+=str(seqnum)+','+line
			ws+='\n'
		else:
			ws+=str(seqnum)+','+line
			ws+='\n'
			seqnum+=1
			ws+=str(seqnum)+','+line
			ws+='\n'

	f=open('R2.csv','w')
	f.write(ws.strip())
	f.close()
if __name__=="__main__":
	main()
