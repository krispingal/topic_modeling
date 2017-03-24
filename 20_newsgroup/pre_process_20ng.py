"""Preprocessing text for analysis 
   includes removing stop-words and then tokenizing
"""
import os
import logging
import gensim
import re
from nltk.corpus import stopwords
from itertools import dropwhile

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

regex_header = re.compile(r"^[a-zA-Z\-]*\:")

def isHeader(s):
    if regex_header.search(s) is None:
        return False
    else:
        return True
        
""" iterate through directories by a  walk"""
def iter_docs(topdir, stoplist):
    for root, subdirs, files in os.walk(topdir):
        for filename in files:
            file_path = os.path.join(root, filename)
            fin = open(file_path, 'rb')
            str_list = []
            for line in dropwhile(isHeader, fin):
               str_list.append(line)
            text = ''.join(str_list)
            fin.close()
            yield (x for x in gensim.utils.tokenize(text, lowercase=True, deacc=True, errors="ignore")
                                                    if x not in stoplist)
 
class OnlineCorpus(object):

    def __init__(self, topdir, stoplist):
        self.topdir = topdir
        self.stoplist = stoplist
        self.dictionary = gensim.corpora.Dictionary(iter_docs(topdir,stoplist))

    def __iter__(self):
        for tokens in iter_docs(self.topdir, self.stoplist):
            yield self.dictionary.doc2bow(tokens)

#TEXTS_DIR = "../Data/mini_newsgroups"
TEXTS_DIR = "../Data/20_newsgroups"
MODELS_DIR = "../Data/models"
stoplist = set(stopwords.words("english")) 

#remove occurences of email id
stoplist.update(["com", "edu"]) 
corpus = OnlineCorpus(TEXTS_DIR, stoplist)
corpus.dictionary.save(os.path.join(MODELS_DIR, 'twentyNewsGroup.dict'))
gensim.corpora.MmCorpus.serialize(os.path.join(MODELS_DIR, 'corpora.mm'), corpus)
