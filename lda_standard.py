import os
import logging
from time import clock

from gensim import corpora, models

MODELS_DIR = "../Data/models"
num_topics = 20
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'twentyNewsGroup.dict'))
corpus = corpora.MmCorpus(os.path.join(MODELS_DIR, 'corpora.mm'))
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
print("Starting LDA with # of topics {0}".format(num_topics)
t0 = clock()
lda = models.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=num_topics)
print("done in %0.3fs." % (clock() - t0))
lda.print_topics(num_topics=num_topics,num_words =10)
lda.save(os.path.join(MODELS_DIR, 'twentyNewsGroups.lda'))
