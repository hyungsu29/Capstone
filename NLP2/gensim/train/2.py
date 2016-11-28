from konlpy.tag import Twitter
from pprint import pprint
from collections import namedtuple
from gensim.models import doc2vec
import sys
doc_vectorizer=doc2vec.Doc2Vec.load('doc2vec.model')

l=list()

for i in range(1,4):
	if(sys.argv[i].strip()=='-1'):
		continue
	l.append(sys.argv[i].strip()+'/Noun')

pprint(doc_vectorizer.most_similar(positive=l))
print (l)
#pprint(doc_vectorizer.most_similar('기말고사/Noun'))
