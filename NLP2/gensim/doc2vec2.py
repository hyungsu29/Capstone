# Import libraries

from gensim.models import doc2vec
from collections import namedtuple

# Load data

doc1 = ["안녕 저는 천재", "안녕 저는 바보"]

# Transform data (you can add more data preprocessing steps) 

docs = []
analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')
for i, text in enumerate(doc1):
    words = text.lower().split()
    tags = [i]
    docs.append(analyzedDocument(words, tags))

# Train model (set min_count = 1, if you want the model to work with the provided example data set)

model = doc2vec.Doc2Vec(docs, size = 100, window = 300, min_count = 1, workers = 4)

# Get the vectors

pl=list()
pl.append("바보")
pl.append("천재")
print (model.most_similar(positive=pl))
