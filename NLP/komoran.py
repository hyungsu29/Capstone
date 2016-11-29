import json
from konlpy.tag import Mecab
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Twitter

import time


useclass=Komoran()


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
		if(i%100==0):
			print (subject)
			print (useclass.nouns(subject))
			print ('===========================================================')
			print (contents)
			print (useclass.nouns(contents))
	end_time=time.time()
	print (end_time-start_time)

if __name__=="__main__":
	main()
