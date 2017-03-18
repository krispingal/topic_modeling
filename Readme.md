Readme
======

[![license](https://img.shields.io/badge/license-MIT%20License-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains my attempts at topic modelling using [gensim][gensim] which is an open source python 
library for topic modelling. Gensim's LDA algorith is an online version which provides many advantages 
such as, it can be applied on corpuses that are larger than RAM available on normal desktops, and it can 
be trained 'forever'. 

First I tried it out on the [20 newsgroup][20_newsgroup] dataset which is a collection 
of 20000 messages/mails from 20 newsgroups.  

There are a few things that I've observed about gensim's LDA behavior

1. The execution timings for lda multicore, does not seem to go down as much as expected, by adding more workers to LDA.
2. I am getting diferent output even after providing the same random state and input corpus to both LDA and HDP.

Requirements
............
Gensim
Numpy
NLTK
A BLAS/LAPACK library (optional)
Mallet (optional)
seaborn (optional)

[gensim]: https://radimrehurek.com/gensim/index.html
[20_newsgroup]: https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups

