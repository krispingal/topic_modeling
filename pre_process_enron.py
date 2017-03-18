"""Preprocessing Enron email text for analysis 
   includes removing stop-words and then tokenizing
"""
import os
import logging
import gensim
import csv
import email
import re
import sys
from time import clock
from nltk.corpus import stopwords

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
csv.field_size_limit(sys.maxsize)

#A simple regex to capture "most" email address
regex_mail = re.compile(r"[a-zA-Z0-9\.]+@[A-Za-z]+.com")

def iter_file(file_name, stoplist=None):
    with open(file_name, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        #skip header
        next(csvfile)
        for row in reader:
            mail_content = []
            raw_msg = email.message_from_string(row[1])
            if raw_msg.is_multipart():
                for payload in raw_msg.get_payload():
                    mail_content.append(payload.get_payload())
            else:
                mail_content.append(raw_msg.get_payload())
            text = ''.join(mail_content)
            text = regex_mail.sub(' ', text, count=0)
            yield (x for x in gensim.utils.tokenize(text, lowercase=True, deacc=True, errors="ignore")
                                                    if x not in stoplist)

TEXTS_FILE = "../Data/enron/emails.csv"
MODELS_DIR = "../Data/models/enron"

class OnlineCorpus(object):

    def __init__(self, file_name, stoplist):
        self.file_name = file_name
        self.stoplist = stoplist
        self.dictionary = gensim.corpora.Dictionary(iter_file(file_name, stoplist))

    def __iter__(self):
        for tokens in iter_file(self.file_name, self.stoplist):
            yield self.dictionary.doc2bow(tokens)

stoplist = set(stopwords.words("english")) 
print("Starting Pre-process \n")
t0 = clock()
corpus = OnlineCorpus(TEXTS_FILE, stoplist)
print("Completed preprocess in {0:.3f} s".format(clock() -t0))
corpus.dictionary.save(os.path.join(MODELS_DIR, 'enron.dict'))
gensim.corpora.MmCorpus.serialize(os.path.join(MODELS_DIR, 'corpora.mm'), corpus)
