from __future__ import print_function
import os
import logging
from argparse import ArgumentParser
from itertools import product
from gensim import corpora, models
from memory_profiler import profile
from time import clock

""" Code to benchmark gensim's LDA on enron email dataset """

#Test dataset
#MODELS_DIR = "../../Data/models/mini_newsgroup"
#Actual dataset
MODELS_DIR = "../../Data/models/enron"
OUT_DIR = "../../Data/out"
MALLET_INSTALLATION_DIR = "../../mallet-2.0.8/bin/mallet" 

topic_out_file = "topic_enron.md"
perf_out_file = "perf_enron.csv"
mem_out_file = "mem_enron.txt"

default_num_test_passes = 3
default_num_words = 20
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

mem_out = open(os.path.join(OUT_DIR, mem_out_file), 'w+')

def parse_args():
    parser = ArgumentParser(description="Benchmark Gensim's LDA on Enron dataset")
    parser.add_argument("--disable_timing", help="Don't measure timing", action="store_true")
    parser.add_argument("--disable_memory", help="Don't measure memory usage", action="store_true")
    parser.add_argument("--disable_topic_words", help="Don't write out top n words", action="store_true")
    parser.add_argument("-w", "--num_words", type=int, default=default_num_words, help="Number of top words to e displayed per topic")
    parser.add_argument("-p", "--num_passes", type=int, default=default_num_test_passes, help="Number of passes to measure timing")
    args = parser.parse_args()
    return args

def cleanup_output_files(args, num_passes, OUT_DIR):
    perf_out = None
    topic_out = None
    if args.disable_timing == False:
        perf_out = open(os.path.join(OUT_DIR, perf_out_file), 'w+')
        #Print column header
        print("implementation, num_topics, iterations, workers, tf-idf", end='', file=perf_out)
        for i in xrange(num_passes):
            print(", pass_{0}".format(i), end='', file=perf_out)
        perf_out.close()
#    if args.disable_memory == False:
#        mem_out = open(os.path.join(OUT_DIR, mem_out_file), 'w+')
    if args.disable_topic_words == False:
        topic_out = open(os.path.join(OUT_DIR, topic_out_file), 'w+')
        topic_out.close()

""" Runs LDA with given params num_passes times to measure performance """
def runLDA_perf(params, num_passes, tf_idf, OUT_DIR, perf_out_file):
    with open(os.path.join(OUT_DIR, perf_out_file), 'a') as fout:
        print("\nGensim, {0}, {1}, {2}, {3}".format(params['num_topics'], params['iterations'], params['workers'], tf_idf), end='', file=fout)
        lda = None
        for i in xrange(num_passes):
            t0 = clock()
            lda = models.ldamulticore.LdaMulticore(**params)
            print(", {0:.3f}".format((clock() - t0)), end='', file=fout)
        print("Completed LDA with params; implementation:Gensim, num_topics:{0}, num_iterations:{1}, num_workers:{2}, tf-idf:{3}".format(params['num_topics'], params['iterations'], params['workers'], tf_idf))
        return lda

""" Run LDA mallet with given params num_passes times to measure performance """
def runLDA_Mallet_perf(params, num_passes, tf_idf, OUT_DIR, perf_out_file):
    with open(os.path.join(OUT_DIR, perf_out_file), 'a') as fout:
        print("\nMallet, {0}, {1}, {2}, {3}".format(params['num_topics'], params['iterations'], params['workers'], tf_idf), end='', file=fout)
        lda = None
        for i in xrange(num_passes):
            t0 = clock()
            lda = models.wrappers.LdaMallet(**params)
            print(", {0:.3f}".format((clock() - t0)), end='', file=fout)
        print("Completed LDA with params; implementation:Mallet, num_topics:{0}, num_iterations:{1}, num_workers:{2}, tf-idf:{3}".format(params['num_topics'], params['iterations'], params['workers'], tf_idf))
        return lda

@profile(stream=mem_out)      
def runLDA_mem(params):
    lda = models.ldamulticore.LdaMulticore(**params)
    return lda

@profile(stream=mem_out)      
def runLDA_Mallet_mem(params):
    lda = models.wrappers.LdaMallet(**params)
    return lda
    
""" Print top num_words associated with each topic """
def print_topics(topic_mat, params, num_words, tf_idf, implementation, OUT_DIR, topic_out_file):
    with open(os.path.join(OUT_DIR, topic_out_file), 'a') as fout:
        print("\nTop {0} words of LDA model with params; implementation:{1}, num_topics:{2}, num_iterations:{3}, num_workers:{4}, tf-idf:{5}\n".format(num_words, 
        implementation, params['num_topics'], params['iterations'], params['workers'], tf_idf), file=fout)
        for topic_id, topic_words in topic_mat:
            print("{0}. Topic id # {1}".format(topic_id+1, topic_id), end=' ', file=fout)
            print([ str(word) for i, (word, prob) in enumerate(topic_words)], file=fout)

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

""" Main function which will dispatch params to appropriate LDA benchmarking functions """
def run_benchmark():
    args = parse_args()
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
    "workers" : [1, 2, 3, 4],
    "tf-idf" : [True, False],
    "implementation" : ["gensim", "mallet"]
    }
    cleanup_output_files(args, args.num_passes, OUT_DIR)
    if (args.disable_timing == False) and (args.disable_memory == False):
        for params in iterate_arguments(param_grid):
            print("Starting with params {0}".format(params))
            params.update({'id2word' : dictionary})
            if params['tf-idf']:
                params.update({'corpus' : corpus_tfidf})
            else :
                params.update({'corpus' : corpus})
            tf_idf = params.pop('tf-idf')
            implementation = params.pop('implementation')
            if implementation == 'gensim':
                lda = runLDA_perf(params, args.num_passes, tf_idf, OUT_DIR, perf_out_file)
                print("Mem testing LDA with params; num_topics:{0}, num_iterations:{1}, num_workers:{2}, tf-idf{3}\n".format(params['num_topics'], params['iterations'], params['workers'], tf_idf), file=mem_out)
                runLDA_mem(params)
                print("Completed")
            elif implementation == 'mallet':
                params.update({"mallet_path" : MALLET_INSTALLATION_DIR})
                lda = runLDA_Mallet_perf(params, args.num_passes, tf_idf, OUT_DIR, perf_out_file)
                print("Mem testing LDA with params; num_topics:{0}, num_iterations:{1}, num_workers:{2}, tf-idf{3}\n".format(params['num_topics'], params['iterations'], params['workers'], tf_idf), file=mem_out)
                runLDA_Mallet_mem(params)
                print("Completed")
            if (args.disable_topic_words == False):
                    topic_mat = lda.show_topics(formatted=False,num_words=args.num_words,num_topics=params['num_topics'])
                    print_topics(topic_mat, params, args.num_words, tf_idf, implementation, OUT_DIR, topic_out_file)
    elif (args.disable_memory == True) and (args.disable_timing == False):
        for params in iterate_arguments(param_grid):
            print("Starting with params {0}".format(params))
            params.update({'id2word' : dictionary})
            if params['tf-idf']:
                params.update({'corpus' : corpus_tfidf})
            else :
                params.update({'corpus' : corpus})
            tf_idf = params.pop('tf-idf')
            implementation = params.pop('implementation')
            if implementation == 'gensim':
                lda = runLDA_perf(params, args.num_passes, tf_idf, OUT_DIR, perf_out_file)
            elif implementation == 'mallet':
                params.update({"mallet_path" : MALLET_INSTALLATION_DIR})
                lda = runLDA_Mallet_perf(params, args.num_passes, tf_idf, OUT_DIR, perf_out_file)
            print("Completed")
            if (args.disable_topic_words == False):
                topic_mat = lda.show_topics(formatted=False,num_words=args.num_words,num_topics=params['num_topics'])
                print_topics(topic_mat, params, args.num_words, tf_idf, implementation, OUT_DIR, topic_out_file)
    elif (args.disable_timing == True) and (args.disable_memory == False):
        for params in iterate_arguments(param_grid):
            print("Starting with params {0}".format(params))
            params.update({'id2word' : dictionary})
            if params['tf-idf']:
                params.update({'corpus' : corpus_tfidf})
            else :
                params.update({'corpus' : corpus})
            tf_idf = params.pop('tf-idf')
            implementation = params.pop('implementation')
            if implementation == 'gensim':
                lda = runLDA_mem(params)
            elif implementation == 'mallet':
                params.update({"mallet_path" : MALLET_INSTALLATION_DIR})
                runLDA_Mallet_mem(params)
            print("Completed")
            if (args.disable_topic_words == False):
                topic_mat = lda.show_topics(formatted=False,num_words=args.num_words,num_topics=params['num_topics'])
                print_topics(topic_mat, params, args.num_words, tf_idf, implementation, OUT_DIR, topic_out_file)
    else :
        print("Nothing to do")
    #close mem_out connection
    mem_out.close()
    print("Finished.")
        
if __name__ == "__main__":
    run_benchmark()
