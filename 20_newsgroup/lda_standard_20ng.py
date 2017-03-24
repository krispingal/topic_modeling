import os
import logging
import numpy as np
from time import clock
from gensim import corpora, models

MODELS_DIR = "../Data/models/lda_standard"
num_topics = 6
num_iterations = 1000
rand_state = 2
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def runLDA(params):
    print("Starting LDA with # of topics {0}".format(params["num_topics"]))
    t0 = clock()
    lda = models.LdaModel(**params)
    print("done in {0:.3f} s".format((clock() - t0)))
    return lda


def displayTopics(topic_mat):
    for topic_id, topic_words in topic_mat:
        print("Topic id # {0}".format(topic_id))
        print([str(word) for i, (word, prob) in enumerate(topic_words)])

if __name__ == "__main__":
    dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'twentyNewsGroup.dict'))
    corpus = corpora.MmCorpus(os.path.join(MODELS_DIR, 'corpora.mm'))
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    params = { 
    "corpus" : corpus_tfidf,
    "id2word" : dictionary,
    "num_topics" : num_topics, 
    "iterations" : num_iterations, 
    "random_state" : rand_state 
    }
    lda = runLDA(params)
    lda.save(os.path.join(MODELS_DIR, 'twentyNewsGroups.lda'))
    topic_mat = lda.show_topics(formatted=False,num_words = 20,num_topics=num_topics)
    displayTopics(topic_mat)
