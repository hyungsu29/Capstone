import json
from konlpy.tag import Mecab
from konlpy.tag import Hannanum
from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Twitter
cls=Twitter()
f=open('dragon2.txt','r')
data=f.read()
f.close()
nouns=cls.nouns(data)
print (nouns)
f=open('dranoun.txt','w')
for noun in nouns:
	f.write(noun+' ')
f.close()
