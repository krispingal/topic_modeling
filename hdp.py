import os
import logging
import numpy as np
from time import clock
from gensim import corpora, models

MODELS_DIR = "../Data/models/hdp"
rand_state = 2
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'twentyNewsGroup.dict'))
corpus = corpora.MmCorpus(os.path.join(MODELS_DIR, 'corpora.mm'))
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
    
print("Starting HDP")
t0 = clock()
hdp = models.hdpmodel.HdpModel(corpus=corpus_tfidf, id2word=dictionary, 
    random_state=rand_state)
print("done in {0:.3f} s".format((clock() - t0)))
hdp.save(os.path.join(MODELS_DIR, 'twentyNewsGroups.hdp'))

topic_mat = hdp.show_topics(formatted=False,num_words = 20,num_topics=6)
for topic_id, topic_words in topic_mat:
    print("Topic id # {0}".format(topic_id))
    print([str(word) for i, (word, prob) in enumerate(topic_words)])


