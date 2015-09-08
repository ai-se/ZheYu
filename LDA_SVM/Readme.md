## A simple try of text mining
#### Dataset:
20 NewsGroups from [Reuters-21578 Text Categorization Collection](http://www.cs.umb.edu/~smimarog/textmining/datasets/)

11293 documents as training set, 7528 documents as test set, all labeled

#### makedata.py
It is a class defined to transfer the orignal data to processable dataset. A vocabulary is made and based on that, dataset with count of word appearance as feature is formed.

#### makemydata.py
Some scripts to load original data and transform them by makedata.py. The results are saved in testdataset.txt, traindataset.txt, trainvoc.txt.

#### LDA_SVM.py
This is a simple try of text mining. 3 methods are tried:
###### a)
LDA first (30 topics), the distribution of topics in each documents are used as new features to do linear SVM.
The resulting accuracy is 65%.
###### b)
LDA first (30 topics), a small group of vocabulary is selected according to the distribution of words in topics. This small group of vocabulary (69 words) is then used as new features to do linear SVM.
The resulting accuracy is 28%. (Probably not a good idea)
###### c)
The original vocabulary (more than 70000 words) is used as features to do linear SVM directly.
The resulting accuracy is ?. (This one will take hours to run)

#### Discussions
LDA can be helpful. The dimension of feature is greatly reduced after doing LDA without losing much information. Actually the result with LDA is slightly better.
The results are not satisfiable.
Reasons can be
######
a) no preprocessing. (For example 'comes' and 'come' should be treated as the same word)
b) words count is not a good feature, tf-idf can be better (according to Rahul's result).
