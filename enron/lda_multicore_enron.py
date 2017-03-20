import os
import logging
from time import clock
from argparse import ArgumentParser
from gensim import corpora, models

MODELS_DIR = "../../Data/models/enron"
#default # of recommended workers is # of cores-1 
default_num_workers = 1
default_num_topics = 10
default_num_iterations = 50
rand_state = 2
#To show topic effectiveness num_words
num_words = 20
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def parse_args():
    parser = ArgumentParser(description="Run gensim's LDA on enron email dataset")
    parser.add_argument('-t', '--num_topics', type=int, default=default_num_topics, help='number of topics')
    parser.add_argument('-w', '--num_workers', type=int, default=default_num_workers, help='number of workers')
    parser.add_argument('-i', '--num_iterations', type=int, default=default_num_iterations, help='number of iterations')
    args = parser.parse_args()
    return args

def runLDA(params):
    print("Starting LDA Multicore on {0} cores, with # of topics {1}".format(params['workers'], params['num_topics']))
    t0 = clock()
    lda = models.ldamulticore.LdaMulticore(**params)
    print("done in {0:.3f} s".format((clock() - t0)))
    return lda

def display_topics(topic_mat):
    for topic_id, topic_words in topic_mat:
        print("Topic id # {0}".format(topic_id))
        print([str(word) for i, (word, prob) in enumerate(topic_words)])

if __name__ == '__main__' :
    args = parse_args()
    dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'enron.dict'))
    corpus = corpora.MmCorpus(os.path.join(MODELS_DIR, 'corpora.mm'))
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    params = {
    "corpus" : corpus_tfidf,
    "id2word" : dictionary,
    "num_topics" : args.num_topics,
    "iterations" : args.num_iterations,
    "workers" : args.num_iterations
    }
    lda = runLDA(params)
    lda.save(os.path.join(MODELS_DIR, 'enron.lda'))
    topic_mat = lda.show_topics(formatted=False,num_words=num_words,num_topics=params['num_topics'])
    display_topics(topic_mat)

