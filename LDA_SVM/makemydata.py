from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division

import pdb
from makedata import *
import numpy as np



trainnum=11293
testnum=7528

trainfile="20ng-train-all-terms.txt"           #20 Newsgroups Dataset from http://www.cs.umb.edu/~smimarog/textmining/datasets/
testfile="20ng-test-all-terms.txt"

training=Data()
training.getdata(trainfile,trainnum)
training.create_vocabulary()
training.create_dataset()

"""
eliminator=np.array(training.dataset)
stc=eliminator[0]
for i in range(1,trainnum):
    stc+=eliminator[i]

voc=[]
for i in range(0,len(training.vocabulary)):
    if stc[i]>100:
        voc.append(training.vocabulary[i])
training.vocabulary=voc


training.create_dataset()
"""

f=open("trainvoc.txt","w")
f.write(str(" ".join(training.vocabulary)))
f.close()
f=open("traindataset.txt","a")
i=0
for data in training.dataset:
    f.write(training.label[i]+" ")
    f.write(" ".join(map(str,data))+'\n')
    i+=1
f.close()

test=Data()
test.getdata(testfile,testnum)
test.vocabulary=training.vocabulary
test.create_dataset()

f=open("testdataset.txt","a")
i=0
for data in test.dataset:
    f.write(test.label[i]+" ")
    f.write(" ".join(map(str,data))+'\n')
    i+=1
f.close()

