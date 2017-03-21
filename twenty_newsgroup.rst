20 newsgroups
=============

The following are the 20 newsgroups:

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

The following is a sample document present in dataset: This was taken from topic sci.electronics.

    Xref: cantaloupe.srv.cs.cmu.edu rec.music.marketplace:4394 misc.forsale:74726 misc.wanted:30876 comp.music:12525 sci.electronics:52720 rec.music.makers.synth:4315
    Newsgroups: rec.music.marketplace,osu.for-sale,misc.forsale,misc.wanted,comp.music,sci.electronics,rec.music.makers.synth
    Path: cantaloupe.srv.cs.cmu.edu!crabapple.srv.cs.cmu.edu!fs7.ece.cmu.edu!europa.eng.gtefsd.com!gatech!udel!wupost!usc!elroy.jpl.nasa.gov!ames!pioneer.arc.nasa.gov!glennd
    From: glennd@pioneer.arc.nasa.gov (Glenn Deardorff)
    Subject: Re: keyboard equipment wanted:
    Message-ID: <1993Apr5.201502.12462@news.arc.nasa.gov>
    Sender: glennd@pioneer.arc.nasa.gov (Glen Deardorff GDP)
    Organization: NASA Ames Res. Ctr. Mtn Vw CA 94035
    References:  <9304041842.AA28793@photon.magnus.acs.ohio-state.edu>
    Date: Mon, 5 Apr 1993 20:15:02 GMT
    Lines: 10
    
    > * Moog, Serge, Paia, or Buchla analogue synthesizer modules or components
    
    > if you have any of the following items, or similar goods, please e-mail or call
    
    Chris (Analog Modular Systems) in L.A. specializes in modular stuff, and I know as of
    last week he has some Serge modules, and perhaps Moog as well.
    
    Number> (213) 850-5216
    
    I just got an Xpander from him - this guy knows how to pack 'em right.

I have benchmarked gensim LDA on this corpus, which can be viewed here: https://github.com/krispingal/topic_modeling/blob/master/lda_benchmark.ipynb.

I get the following top 20 words for 6 topics, as output while running **gensim LDA** on 20-newsgroups for 6 topics *with tf-idf*.

1. Topic id # 0 ['cunyvm', 'foxvog', 'vtt', 'huston', 'tko', 'dfo', 'waldrop', 'tesrt', 'tufts', 'announcing', 'fusi', 'nis', 'chuvashia', 'inguiry', 'eridan', 'daruwala', 'vrrend', 'ich', 'harvested', 'jade']
2. Topic id # 1 ['maine', 'sfu', 'callison', 'oehler', 'bcci', 'dta', 'mattias', 'bobc', 'rauser', 'camosun', 'krzysztof', 'captain', 'albany', 'maynard', 'cbda', 'apgea', 'oasys', 'cuesta', 'lockridge', 'mydisplay']
3. Topic id # 2 [\'_', 'would', 'card', 'people', 'x', 'one', 'government', 'c', 'get', 'like', 'know', 'please', 'article', 'thanks', 'use', 'think', 'anyone', 'drive', 'writes', 'also']
4. Topic id # 3 ['russotto', 'jpeg', 'gsh', 'slac', 'hennessy', 'jb', 'bigboote', 'victor', 'scodal', 'shearson', 'usl', 'wam', 'charlottesville', 'higgins', 'nswc', 'intercon', 'oo', 'srl', 'slacvm', 'ucf']
5. Topic id # 4 ['truelove', 'leftover', 'mpr', 'inescn', 'hess', 'porto', 'kwansik', 'turkey', 'tracy', 'pom', 'sandia', 'casserole', 'tlu', 'gic', 'ming', 'christmas', 'sylvain', 'chalmers', 'mgp', 'unh']
6. Topic id # 5 ['windows', 'graphics', 'scsi', 'ide', 'files', 'x', 'dos', 'controller', 'thanks', 'drive', 'batf', 'fbi', 'file', 'program', 'disk', 'images', 'bus', 'pc', 'format', 'ram']

and the following also from **gensim LDA**, but this time *without tf-idf* transformation.

1. Topic id # 0 ['people', 'would', 'one', 'government', 'writes', 'law', 'god', 'us', 'fbi', 'article', 'think', 'said', 'believe', 'right', 'even', 'many', 'may', 'children', 'say', 'also']
2. Topic id # 1 ['article', 'writes', 'graphics', 'apr', 'one', 'ca', 'news', 'would', 'c', 'cs', 'lines', 'modem', 'good', 'university', 'cd', 'think', 'like', 'new', 'know', 'washington']
3. Topic id # 2 [\'_', 'package', 'would', 'writes', 'article', 'apr', 'one', \'__', \'___', 'mode', 'digital', 'know', 'like', 'new', 'e', 'university', 'also', 'colors', 'could', 'get']
4. Topic id # 3 ['x', 'w', 'c', 'r', 'e', 'v', 'p', 'b', 'k', 'u', 'g', 'n', 'z', 'file', 'h', 'f', 'image', 'l', 'j', 'windows']
5. Topic id # 4 ['would', 'one', 'get', 'like', 'know', 'writes', 'use', 'article', 'think', 'time', 'want', 'good', 'well', 'also', 'much', 'dos', 'people', 'could', 'problem', 'two']
6. Topic id # 5 ['ax', 'q', 'f', 'max', 'g', 'p', 'u', 'mb', 'b', 'r', 'v', 'x', 'n', 'e', 'l', 'c', 'z', 'w', 'clipper', 'j']

I get the following top 20 words for 6 topics, as output while running **gensim LDA mallet wrapper** on 20-newsgroups for 6 topics *with tf-idf*.

1. Topic id # 0 ['good', 'r_z', 'uus', 'uuw', 'vrvrtv', 'alyzfo', 'ikh', 'ikai', 'ikl', 'mwbel', \'uu_', 'cvi', 'pdz', 'azzq', 'hhpl', 'sty', 'wkx', 'ystg', 'z_c_', 'uum']
2. Topic id # 1 ['tesrt', 'uuw', 'uum', 'xgyu', 'r_z', 'alyzfo', 'ikh', 'ikai', 'ikl', 'mwbel', \'uu_', 'cvi', 'pdz', 'azzq', 'hhpl', 'sty', 'wkx', 'ikj', 'z_c_', 'vrvrtv']
3. Topic id # 2 ['satan', 'test', 'bullshit', 'ikh', 'uuw', 'vrvrtv', 'alyzfo', 'ikai', 'ikl', 'mwbel', \'uu_', 'cvi', 'pdz', 'azzq', 'hhpl', 'sty', 'wkx', 'ikj', 'uus', 'z_c_']
4. Topic id # 3 ['test', 'exit', 'r_z', 'uus', 'uuw', 'vrvrtv', 'alyzfo', 'ikh', 'ikai', 'ikl', 'mwbel', \'uu_', 'cvi', 'pdz', 'azzq', 'hhpl', 'sty', 'wkx', 'z_c_', 'uum']
5. Topic id # 4 ['unsubscribe', 'kidding', 'test', 'ignore', 'xgyu', 'ikh', 'alyzfo', 'ikai', 'ikl', 'mwbel', \'uu_', 'cvi', 'pdz', 'azzq', 'hhpl', 'sty', 'wkx', 'ikj', 'vrvrtv', 'uum']
6. Topic id # 5 ['ken', 'ikh', 'uus', 'uuw', 'vrvrtv', 'r_z', 'alyzfo', 'ikai', 'ikl', 'mwbel', \'uu_', 'cvi', 'pdz', 'azzq', 'hhpl', 'sty', 'wkx', 'ikj', 'z_c_', 'uum']  

I get the following top 20 words for 6 topics, as output while running **gensim LDA mallet wrapper** on 20-newsgroups for 6 topics *without tf-idf*.

1. Topic id # 0 ['god', 'people', 'writes', 'time', 'good', 'article', 'point', 'jesus', 'question', 'make', 'fact', 'true', 'life', 'things', 'read', 'man', 'wrong', 'find', 'christian', 'world']
2. Topic id # 1 ['_', 'car', 'drive', 'power', 'buy', 'price', \'__', 'good', \'___', 'apple', 'speed', 'uiuc', 'hp', 'cars', 'problem', 'sale', 'monitor', 'hard', 'bought', 'mb']
3. Topic id # 2 ['ax', 'writes', 'article', 'apr', 'max', 'cs', 'ca', 'lines', 'news', 'university', 'organization', 'netcom', 'org', 'posting', \'_', 'cc', 'uk', 'bike', 'dod', 'pl']
4. Topic id # 3 ['year', 'game', 'space', 'time', 'good', 'team', 'years', 'back', 'play', 'games', 'nasa', 'ca', 'long', 'high', 'win', 'hockey', 'research', 'hit', 'players', 'season']
5. Topic id # 4 ['people', 'government', 'state', 'law', 'gun', 'israel', 'time', 'rights', 'president', 'public', 'children', 'fbi', 'states', 'war', 'fire', 'today', 'jews', 'mr', 'make', 'years']
6. Topic id # 5 ['system', 'windows', 'file', 'bit', 'mail', 'program', 'data', 'software', 'information', 'key', 'dos', 'computer', 'version', 'image', 'card', 'files', 'work', 'run', 'problem', 'graphics']

As you can notice there is significant difference between the one from gensim as well as the one from mallet.
Running both library's LDA on same dataset I noticed:  
Gensim seems to perform better with corpuses that underwent tf-idf transformation.
Mallet seems to perform very well with regular corpuses but performs badly with tf-idf transformed corpus. 

I am inclining more towards Mallet's LDA with no tf-idf transformation, as it seems to give out more words which I know of to belong in same topic.
One way to qualitatively measure accuracy between thse two models, would be to hold out some documents, and later test these documents on our model 
and see which one correctly predicts the topics the most.

Finally I decided to try out HDP on this dataset.
I get the following top 20 words as output while running HDP, the non prameterised version of LDA, on 20-newsgroups for 6 topics.

1. Topic id # 0 ['would', 'one', 'people', 'x', 'like', 'know', 'get', 'c', 'think', 'god', 'article', 'writes', 'use', \'_', 'apr', 'time', 'also', 'could', 'anyone', 'new']
2. Topic id # 1 ['x', 'would', 'windows', 'one', 'know', 'thanks', 'drive', 'c', 'get', 'like', 'anyone', 'people', 'use', 'article', 'please', 'writes', 'apr', 'card', 'cs', \'_']
3. Topic id # 2 ['god', 'morality', 'cobb', 'would', 'uiuc', 'lis', 'know', 'thanks', 'one', 'anyone', 'get', 'could', 'think', 'ico', 'writes', 'objective', 'system', 'x', 'like', 'someone']
4. Topic id # 3 ['religion', 'x', 'rb', \'_', 'qur', 'cookson', 'thanks', 'mitre', 'god', 'switch', 'islam', 'engr', 'posting', 'timessqr', 'know', 'latech', 'get', 'bike', 'c', 'low']
5. Topic id # 4 ['mabe', 'lars_jorgensen', 'sex', 'new', 'bmug', 'way', 'black', 'monash', 'bike', 'please', 'war', 'gregg', 'would', 'uk', 'audibly', 'writes', 'jaeger', 'clutch', 'book', 'opinions']
6. Topic id # 5 ['objective', 'horizon', 'atheism', 'black', 'would', 'event', 'writes', 'values', 'moral', 'mathew', 'mantis', 'frank', 'reality', 'could', 'thanks', 'look', 'minar', 'milwaukeeans', 'send', 'itsmail']
