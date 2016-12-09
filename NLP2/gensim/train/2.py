from konlpy.tag import Twitter
from pprint import pprint
from collections import namedtuple
from gensim.models import doc2vec
import sys
doc_vectorizer=doc2vec.Doc2Vec.load('doc2vec.model')

l=list()
l2=list()
for i in range(1,10):
	if(sys.argv[i].strip()=='-1'):
		continue
	if(sys.argv[i].strip()[0]=='-'):
		l2.append(sys.argv[i].strip()[1:]+'/Noun')
	else:
		l.append(sys.argv[i].strip()+'/Noun')

pprint(doc_vectorizer.most_similar(positive=l, negative=l2, topn=30))
print (l)
print (l2)
#pprint(doc_vectorizer.most_similar('기말고사/Noun'))
