from __future__ import print_function
import os
import logging
from time import clock
from itertools import product
from gensim import corpora, models
""" Code to benchmark gensim's LDA on enron email dataset """

MODELS_DIR = "../../Data/models/enron"
num_test_passes = 3
num_words = 20
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
topic_out_file = "../../Data/out/topic_enron.rst"
perf_out_file = "../../Data/out/perf_enron.txt"

def runLDA(params, perf_out_file):
    with open(perf_out_file, 'a') as fout:
        print("Starting benchmark with params; num_topics:{0}, num_iterations:{1}, num_workers:{2}".format(params['num_topics'], params['iterations'], params['workers']), file=fout)
        lda = None
        for i in xrange(num_test_passes):
            print(" iteration {0}".format(i), end=' ', file=fout)
            t0 = clock()
            lda = models.ldamulticore.LdaMulticore(**params)
            print("done in {0:.3f} s".format((clock() - t0)), file=fout)
        print("Completed LDA with params : {0}".format(params))
        return lda

def print_topics(topic_mat, params, file_name):
    with open(file_name, 'a') as fout:
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
        lda = runLDA(params, perf_out_file)
        print("Completed")
        topic_mat = lda.show_topics(formatted=False,num_words=num_words,num_topics=params['num_topics'])
        print_topics(topic_mat, params, topic_out_file)
    
if __name__ == "__main__":
    dictionary = corpora.Dictionary.load(os.path.join(MODELS_DIR,'enron.dict'))
    corpus = corpora.MmCorpus(os.path.join(MODELS_DIR, 'corpora.mm'))
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    param_grid = {
    "num_topics" : [5, 10, 20, 30, 40],
    "iterations" : [50, 100, 300, 600, 1000]
    "workers" : [None, 1, 2, 3, 4]
    }
    run_benchmark(param_grid, corpus_tfidf, dictionary, perf_out_file, topic_out_file)
