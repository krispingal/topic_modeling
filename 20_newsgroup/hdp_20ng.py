import os
import logging
import numpy as np
from time import clock
from argparse import ArgumentParser
from gensim import corpora, models

MODELS_DIR = "../../Data/models/hdp"
rand_state = 2
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

default_num_topics = 6
default_num_workers = 1
default_num_iterations = 50

def parse_args():
    parser = ArgumentParser(description="Run gensim's HDP on 20 newsgroup data")
    parser.add_argument('-t', '--num_topics', type=int, default=default_num_topics, help='number of topics')
    parser.add_argument('--enable_tf_idf', action="store_true", help="Perform tf-idf transformation before providing corpus to hdp")
    args = parser.parse_args()
    return args

def runHdp(params):
    print("Starting HDP")
    t0 = clock()
    hdp = models.hdpmodel.HdpModel(**params)
    print("done in {0:.3f} s".format((clock() - t0)))
    return hdp
 
def display_topics(topic_mat):   
    for topic_id, topic_words in topic_mat:
        print("Topic id # {0}".format(topic_id))
        print([str(word) for i, (word, prob) in enumerate(topic_words)])

if __name__ == '__main__':
    args = parse_args()
    dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'twentyNewsGroup.dict'))
    corpus = corpora.MmCorpus(os.path.join(MODELS_DIR, 'corpora.mm'))
    params = {
    "id2word" : dictionary,
    }
    if args.enable_tf_idf :
        tfidf = models.TfidfModel(corpus)
        corpus_tfidf = tfidf[corpus]
        params.update({ 'corpus' : corpus_tfidf})
    else :
        params.update({ 'corpus' : corpus})
    hdp = runHdp(params)
    hdp.save(os.path.join(MODELS_DIR, 'twentyNewsGroups.hdp'))
    topic_mat = hdp.show_topics(formatted=False,num_words = 20,num_topics=args.num_topics)
    display_topics(topic_mat)
