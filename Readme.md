Readme
======

[![license](https://img.shields.io/badge/license-MIT%20License-blue.svg)](https://opensource.org/licenses/MIT)

This repository contains my attempts at topic modelling using [gensim][gensim] which is an open source python 
library for topic modelling. Gensim's LDA algorith is an online version which provides many advantages 
such as, it can be applied on corpuses that are larger than RAM available on normal desktops, and it can 
be trained 'forever'. Firstly I am trying it out on the [20 newsgroup][20_newsgroup] dataset which is a collection 
of 20000 messages/mails from 20 newsgroups. The following are the 20 newsgroups:

1. alt.atheism                
2. comp.graphics              
3. comp.os.ms-windows.misc    
4. comp.sys.ibm.pc.hardware   
5. comp.sys.mac.hardware      
6. comp.windows.x             
7. misc.forsale      
8. rec.autos                  
9. rec.motorcycles    
10. rec.sport.baseball 
11. rec.sport.hockey   
12. sci.crypt          
13. sci.electronics    
14. sci.med
15. sci.space
16. soc.religion.christian
17. talk.politics.guns
18. talk.politics.mideast
19. talk.politics.misc
20. talk.religion.misc

I have benchmarked gensim LDA on this corpus, which can be viewed [here][lda_benchmark]

I get the following top 20 words as output while running LDA on 20-newsgroups for 6 topics.

1. Topic id # 0 ['cunyvm', 'foxvog', 'vtt', 'huston', 'tko', 'dfo', 'waldrop', 'tesrt', 'tufts', 'announcing', 'fusi', 'nis', 'chuvashia', 'inguiry', 'eridan', 'daruwala', 'vrrend', 'ich', 'harvested', 'jade']
2. Topic id # 1 ['maine', 'sfu', 'callison', 'oehler', 'bcci', 'dta', 'mattias', 'bobc', 'rauser', 'camosun', 'krzysztof', 'captain', 'albany', 'maynard', 'cbda', 'apgea', 'oasys', 'cuesta', 'lockridge', 'mydisplay']
3. Topic id # 2 ['_', 'would', 'card', 'people', 'x', 'one', 'government', 'c', 'get', 'like', 'know', 'please', 'article', 'thanks', 'use', 'think', 'anyone', 'drive', 'writes', 'also']
4. Topic id # 3 ['russotto', 'jpeg', 'gsh', 'slac', 'hennessy', 'jb', 'bigboote', 'victor', 'scodal', 'shearson', 'usl', 'wam', 'charlottesville', 'higgins', 'nswc', 'intercon', 'oo', 'srl', 'slacvm', 'ucf']
5. Topic id # 4 ['truelove', 'leftover', 'mpr', 'inescn', 'hess', 'porto', 'kwansik', 'turkey', 'tracy', 'pom', 'sandia', 'casserole', 'tlu', 'gic', 'ming', 'christmas', 'sylvain', 'chalmers', 'mgp', 'unh']
6. Topic id # 5 ['windows', 'graphics', 'scsi', 'ide', 'files', 'x', 'dos', 'controller', 'thanks', 'drive', 'batf', 'fbi', 'file', 'program', 'disk', 'images', 'bus', 'pc', 'format', 'ram']

I get the following top 20 words as output while running HDP, the non prameterised version of LDA, on 20-newsgroups for 6 topics.

1. Topic id # 0 ['would', 'one', 'people', 'x', 'like', 'know', 'get', 'c', 'think', 'god', 'article', 'writes', 'use', '_', 'apr', 'time', 'also', 'could', 'anyone', 'new']
2. Topic id # 1 ['x', 'would', 'windows', 'one', 'know', 'thanks', 'drive', 'c', 'get', 'like', 'anyone', 'people', 'use', 'article', 'please', 'writes', 'apr', 'card', 'cs', '_']
3. Topic id # 2 ['god', 'morality', 'cobb', 'would', 'uiuc', 'lis', 'know', 'thanks', 'one', 'anyone', 'get', 'could', 'think', 'ico', 'writes', 'objective', 'system', 'x', 'like', 'someone']
4. Topic id # 3 ['religion', 'x', 'rb', '_', 'qur', 'cookson', 'thanks', 'mitre', 'god', 'switch', 'islam', 'engr', 'posting', 'timessqr', 'know', 'latech', 'get', 'bike', 'c', 'low']
5. Topic id # 4 ['mabe', 'lars_jorgensen', 'sex', 'new', 'bmug', 'way', 'black', 'monash', 'bike', 'please', 'war', 'gregg', 'would', 'uk', 'audibly', 'writes', 'jaeger', 'clutch', 'book', 'opinions']
6. Topic id # 5 ['objective', 'horizon', 'atheism', 'black', 'would', 'event', 'writes', 'values', 'moral', 'mathew', 'mantis', 'frank', 'reality', 'could', 'thanks', 'look', 'minar', 'milwaukeeans', 'send', 'itsmail']

There are a few things that I've observed about gensim's LDA behavior

1. The execution timings for lda multicore does not seem to go down as expected by adding more workers to LDA.
2. I am getting diferent output even after providing the same random state and imput corpus to both LDA and HDP.

[gensim]: https://radimrehurek.com/gensim/index.html
[20_newsgroup]: https://archive.ics.uci.edu/ml/datasets/Twenty+Newsgroups
[lda_benchmark]: https://github.com/krispingal/topic_modeling/blob/master/lda_benchmark.ipynb
