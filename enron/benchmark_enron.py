from __future__ import print_function
import os
import logging
from time import clock
from itertools import product
from memory_profiler import profile
from gensim import corpora, models

""" Code to benchmark gensim's LDA on enron email dataset """

#Test dataset
MODELS_DIR = "../../Data/models/mini_newsgroup"
#Actual dataset
#MODELS_DIR = "../../Data/models/enron"
OUT_DIR = "../../Data/out"

topic_out_file = "topic_enron.rst"
perf_out_file = "perf_enron.csv"
mem_out_file = "mem_enron.txt"

num_test_passes = 3
num_words = 20
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


mem = open(os.path.join(OUT_DIR, mem_out_file), 'w+')

""" Runs LDA with given params num_test_passes times to measure performance """
def runLDA_perf(params, perf_out_file):
    with open(os.path.join(OUT_DIR, perf_out_file), 'a') as fout:
        print("\n{0}, {1}, {2}".format(params['num_topics'], params['iterations'], params['workers']), end='', file=fout)
        lda = None
        for i in xrange(num_test_passes):
            t0 = clock()
            lda = models.ldamulticore.LdaMulticore(**params)
            print(", {0:.3f}".format((clock() - t0)), end='', file=fout)
        print("Completed LDA with params; num_topics:{0}, num_iterations:{1}, num_workers:{2}".format(params['num_topics'], params['iterations'], params['workers']))
        return lda

@profile(stream=mem)      
def runLDA_mem(params):
    models.ldamulticore.LdaMulticore(**params)

def print_topics(topic_mat, params, file_name):
    with open(os.path.join(OUT_DIR, file_name), 'a') as fout:
        print("\nTop {0} words of LDA model with params; num_topics:{1}, num_iterations:{2}, num_workers:{3}\n".format(num_words, params['num_topics'], params['iterations'], params['workers']), file=fout)
        for topic_id, topic_words in topic_mat:
            print("{0}. Topic id # {1}".format(topic_id+1, topic_id), end=' ', file=fout)
            print([str(word) for i, (word, prob) in enumerate(topic_words)], file=fout)

def iterate_arguments(param_grid):
    # Sort the keys of a dict for reproducibility
    items = sorted(param_grid.items())
    if not items:
        yield {}
    else:
        keys, values = zip(*items)
        for v in product(*values):
            params = dict(zip(keys, v))
            yield params

def run_benchmark(param_grid, corpus, dictionary, perf_out_file, topic_out_file):
    for params in iterate_arguments(param_grid):
        print("Starting with params {0}".format(params))
        params.update({'corpus' : corpus, 'id2word' : dictionary})
        lda = runLDA_perf(params, perf_out_file)
        print("Mem testing LDA with params; num_topics:{0}, num_iterations:{1}, num_workers:{2}\n".format(params['num_topics'], params['iterations'], params['workers']), file=mem)
        runLDA_mem(params)
        print("Completed")
        topic_mat = lda.show_topics(formatted=False,num_words=num_words,num_topics=params['num_topics'])
        print_topics(topic_mat, params, topic_out_file)
    
if __name__ == "__main__":
    #Test Dictionary
    dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'twentyNewsGroup.dict'))
    #Actual Dictionary
    #dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'enron.dict'))
    corpus = corpora.MmCorpus(os.path.join(MODELS_DIR, 'corpora.mm'))
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    param_grid = {
    "num_topics" : [5, 10, 20, 30, 40],
    "iterations" : [50, 100, 300, 600, 1000],
    "workers" : [None, 1, 2, 3, 4]
#    "implementation" : ["gensim", "mallet"]
    }
    run_benchmark(param_grid, corpus_tfidf, dictionary, perf_out_file, topic_out_file)
