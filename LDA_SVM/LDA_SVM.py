from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division
from sklearn import svm
from makedata import *
import numpy as np
import lda
import matplotlib.pyplot as plt
import pdb
try:
    plt.style.use('ggplot')
except:
    # version of matplotlib might not be recent
    pass




trainfile="20ng-train-all-terms.txt"           #20 Newsgroups Dataset from http://www.cs.umb.edu/~smimarog/textmining/datasets/
testfile="20ng-test-all-terms.txt"

training=Data()
training.get_vocabulary("trainvoc.txt")
training.get_dataset("traindataset.txt")
test=Data()
test.get_dataset("testdataset.txt")

trainnum=training.docnum
testnum=test.docnum
docnum=trainnum+testnum


X = np.array(training.dataset+test.dataset)
vocab = np.array(training.vocabulary)
SVM_train_label = np.array(training.label)
SVM_test_label = np.array(test.label)

topicsnum=30
iternum=500

model = lda.LDA(n_topics=topicsnum, n_iter=iternum, random_state=1)
model.fit(X)
topic_word = model.topic_word_
doc_topic = model.doc_topic_


# use topic distribution in documents as features to do SVM

SVM_train_data=doc_topic[:trainnum,:].tolist()
SVM_test_data=doc_topic[trainnum:,:].tolist()
SVM_train_label=SVM_train_label.tolist()
SVM_test_label=SVM_test_label.tolist()

clf = svm.SVC()
clf.fit(SVM_train_data, SVM_train_label)
SVM_predict=clf.predict(SVM_test_data)

count=0
for i in range(0,len(SVM_predict)):
    if SVM_predict[i]==SVM_test_label[i]:
        count+=1
accuracy=count/len(SVM_predict)
print("SVM_topics: %s" % accuracy)

# use high value words in lda topics as features to do SVM

word_lst=[]
n_top_words = 10
for i, topic_dist in enumerate(topic_word):
    topic_words =np.argsort(topic_dist)[:-n_top_words:-1]
    word_lst+=topic_words.tolist()
word_lst2=[]
word_lst2.append(word_lst[0])
for i in range(1,len(word_lst)):
    flag=True
    for word in word_lst2:
        if word==word_lst[i] : flag=False
    if flag:  word_lst2.append(word_lst[i])


pdb.set_trace()
SVM_train_data=np.array(training.dataset)[:,word_lst2].tolist()
SVM_test_data=np.array(test.dataset)[:,word_lst2].tolist()

clf2 = svm.SVC()
clf2.fit(SVM_train_data, SVM_train_label)
SVM_predict=clf2.predict(SVM_test_data)

count=0
for i in range(0,len(SVM_predict)):
    if SVM_predict[i]==SVM_test_label[i]:
        count+=1
accuracy=count/len(SVM_predict)
print("SVM_words: %s" % accuracy)

############################# SVM only
clf3 = svm.SVC()
clf3.fit(training.dataset, SVM_train_label)
SVM_predict=clf3.predict(test.dataset)

count=0
for i in range(0,len(SVM_predict)):
    if SVM_predict[i]==SVM_test_label[i]:
        count+=1
accuracy=count/len(SVM_predict)
print("SVM_only: %s" % accuracy)

"""



f, ax= plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([1, 3, 4, 8, 9]):
    ax[i].stem(doc_topic[k,:], linefmt='r-',
               markerfmt='ro', basefmt='w-')
    ax[i].set_xlim(-1, topicsnum+1)
    ax[i].set_ylim(0, 1)
    ax[i].set_ylabel("Prob")
    ax[i].set_title("Document {}".format(k))

ax[4].set_xlabel("Topic")

plt.tight_layout()
plt.show()

"""