import os
import logging
from argparse import ArgumentParser
from time import clock
from gensim import corpora, models

MODELS_DIR = "../../Data/models/lda_multicore"
MALLET_INSTALLATION_DIR = "../../mallet-2.0.8/bin/mallet" 
default_num_topics = 6
default_num_iterations = 1000
rand_state = 2
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def parse_args():
    parser = ArgumentParser(description="Run Mallet's LDA on 20 newsgroup dataset")
    parser.add_argument('-t', '--num_topics', type=int, default=default_num_topics, help='number of topics')
    parser.add_argument('-i', '--num_iterations', type=int, default=default_num_iterations, help='number of iterations')
    parser.add_argument('--enable_tf_idf', action='store_true', help='Perform tf-idf transformation on corpus')
    args = parser.parse_args()
    return args

""" Run Mallet's LDA on 20 newsgroup using gensim's wrapper """
def runLDAMallet(params):
    print("Starting LDA Mallet, with # of topics {0}".format(params["num_topics"]))
    t0 = clock()
    lda = models.wrappers.LdaMallet(**params)
    print("done in {0:.3f} s".format((clock() - t0)))
    return lda

def displayTopics(topic_mat):
    for topic_id, topic_words in topic_mat:
        print("Topic id # {0}".format(topic_id))
        print([str(word) for i, (word, prob) in enumerate(topic_words)])

if __name__ == "__main__":
    args = parse_args()
    dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'twentyNewsGroup.dict'))
    corpus = corpora.MmCorpus(os.path.join(MODELS_DIR, 'corpora.mm'))
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    params = { 
    "id2word" : dictionary,
    "num_topics" : args.num_topics,
    "iterations" : args.num_iterations,
    "mallet_path" : MALLET_INSTALLATION_DIR
    }
    if args.enable_tf_idf:
        params.update({'corpus' : corpus_tfidf })
    else :
        params.update({'corpus' : corpus })
    lda = runLDAMallet(params)
    lda.save(os.path.join(MODELS_DIR, 'twentyNewsGroups.lda'))
    topic_mat = lda.show_topics(formatted=False,num_words = 20,num_topics=args.num_topics)
    displayTopics(topic_mat)
    cm = models.CoherenceModel(model=lda, corpus=params['corpus'], dictionary=dictionary, coherence='u_mass')
    print("UMass Coherence of model: {0}".format(cm.get_coherence()))

