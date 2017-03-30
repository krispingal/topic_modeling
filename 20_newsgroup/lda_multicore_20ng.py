import os
import logging
from time import clock

from gensim import corpora, models

MODELS_DIR = "../../Data/models/lda_multicore"
#default # of recommended workers is # of cores-1 
num_workers = 3
num_topics = 6
rand_state = 2
num_iterations = 1000
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'twentyNewsGroup.dict'))
corpus = corpora.MmCorpus(os.path.join(MODELS_DIR, 'corpora.mm'))
tfidf = models.TfidfModel(corpus)
corpus_tfidf = tfidf[corpus]
    
print("Starting LDA Multicore on {0} cores, with # of topics {1}".format(num_workers, num_topics))
t0 = clock()
lda = models.ldamulticore.LdaMulticore(corpus=corpus_tfidf, id2word=dictionary, 
    num_topics=num_topics, workers=num_workers, random_state=rand_state)
print("done in {0:.3f} s".format((clock() - t0)))

lda.save(os.path.join(MODELS_DIR, 'twentyNewsGroups.lda'))
topic_mat = lda.show_topics(formatted=False,num_words=20,num_topics=num_topics)

for topic_id, topic_words in topic_mat:
    print("Topic id # {0}".format(topic_id))
    print([str(word) for i, (word, prob) in enumerate(topic_words)])
