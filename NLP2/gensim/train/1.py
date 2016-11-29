def read_data(filename):
    with open(filename, 'r') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        data = data[1:]   # header 제외
    return data
train_data = read_data('train.txt')


print(len(train_data))      # nrows: 150000
print(len(train_data[0]))

from konlpy.tag import Twitter
pos_tagger = Twitter()
def tokenize(doc):
    # norm, stem은 optional
    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]
train_docs=list()
for row in train_data:
	try:
		train_docs.append((tokenize(row[1]), row[2]))
	except:
		continue
#train_docs = [(tokenize(row[1]), row[2]) for row in train_data]

from pprint import pprint
pprint(train_docs[0])

from collections import namedtuple
TaggedDocument = namedtuple('TaggedDocument', 'words tags')
tagged_train_docs = [TaggedDocument(d, [c]) for d, c in train_docs]

from gensim.models import doc2vec
# 사전 구축
doc_vectorizer = doc2vec.Doc2Vec(size=300, alpha=0.025, min_alpha=0.025, seed=1234)
doc_vectorizer.build_vocab(tagged_train_docs)
# Train document vectors!
for epoch in range(10):
    print (epoch)
    doc_vectorizer.train(tagged_train_docs)
    doc_vectorizer.alpha -= 0.002  # decrease the learning rate
    doc_vectorizer.min_alpha = doc_vectorizer.alpha  # fix the learning rate, no decay
# To save
doc_vectorizer.save('doc2vec.model')




pprint(doc_vectorizer.most_similar('중간고사/Noun'))
