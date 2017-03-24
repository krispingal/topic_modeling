Readme
======

[![license](https://img.shields.io/badge/license-MIT%20License-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains my attempts at topic modelling using [gensim][gensim] which is an open source python 
library for topic modelling. Gensim's LDA algorithm is an online version which provides many advantages 
such as, it can be applied on corpuses that are larger than RAM available on normal desktops, and it can 
be trained 'forever'. 

First I tried it out on the [20 newsgroup][20_newsgroup] dataset which is a collection 
of 20,000 messages/mails from 20 newsgroups. You can see the results I got [here][20_ng]

Next I tried LDA on a bigger data set, the [enron email data set][enron_kaggle] 
which is a collection of around 500,000 mails from employees of Enron. I used the dataset that was published in [kaggle][kaggle] which is in csv format.
You can try this alternate [url][enron] to get the same data set but in individual file format.

There are a few things that I've observed about gensim's LDA behavior

1. The execution timings for lda multicore, does not seem to go down as much as expected, by adding more workers to LDA.
2. I am getting diferent output even after providing the same random state and input corpus to both LDA and HDP.

Requirements
------------

* [Gensim][gensim]
* Numpy
* [NLTK][nltk]
* A BLAS/LAPACK library (optional)
* [Mallet][mallet] (optional)
* [seaborn][sns] (optional)

[gensim]: https://radimrehurek.com/gensim/index.html
[20_newsgroup]: https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups
[20_ng]: https://github.com/krispingal/topic_modeling/blob/master/twenty_newsgroup.rst
[enron_kaggle]: https://www.kaggle.com/wcukierski/enron-email-dataset
[kaggle]: https://www.kaggle.com/
[enron]: https://www.cs.cmu.edu/~./enron/
[nltk]: http://www.nltk.org/
[mallet]: http://mallet.cs.umass.edu/
[sns]: https://seaborn.pydata.org/index.html
