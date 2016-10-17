import json
from konlpy.tag import Mecab
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Twitter

import time


useclass=list()
useclass.append(Komoran())
useclass.append(Mecab())
useclass.append(Twitter())

FILEPATH="./data.json"
DATA={}

def readjson(fn):
	f=open(fn,'r')
	js=json.loads(f.read())
	f.close()
	return js

def main():
	start_time=time.time()
	global FILEPATH
	global DATA
	DATA=readjson(FILEPATH)
	i=0
	for data in DATA:
		i+=1
		no=data['no']
		date=data['date']
		subject=data['subject']
		contents=data['contents']
		dt=dict()
		if(i%50==0):
			for j in range(0, 3):
				no1=useclass[j].nouns(subject)
				no2=useclass[j].nouns(contents)
				for d in no1:
					if (d in dt):
						dt[d][j]+=1
					else:
						dt[d]=list()
						dt[d].append(0)
						dt[d].append(0)
						dt[d].append(0)
						dt[d][j]=1
				for d in no2:
					if (d in dt):
						dt[d][j]+=1
					else:
						dt[d]=list()
						dt[d].append(0)
						dt[d].append(0)
						dt[d].append(0)
						dt[d][j]=1
			#print (dt)
			pl=list()
			for d in dt.items():
				flag=1
				if(d[1][0]+d[1][1]==0):
					flag=0
				if(d[1][0]+d[1][2]==0):
					flag=0
				if(d[1][1]+d[1][2]==0):
					flag=0
				if(flag==1):
					pl.append(d[0])
			print (pl)
			print ('============================================================')
	end_time=time.time()
	print (end_time-start_time)

if __name__=="__main__":
	main()
