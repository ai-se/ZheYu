from __future__ import print_function, unicode_literals
from __future__ import absolute_import, division

class Data(object):



    def __init__(self):
        self.data=[]
        self.dataset=[]
        self.label=[]
        self.docnum=0
        self.vocabulary=[]

    def getdata(self,file,num):
        f=open(file,"r")
        self.docnum=num
        for i in range(0,num):
            read=f.readline()
            x=0
            self.data.append([])
            for j in range(0,len(read)):
                if read[j]==' ' or read[j]=='\n' or read[j]=='\t':
                    self.data[i].append(read[x:j])
                    x=j+1
        f.close()

    def create_vocabulary(self):
        self.vocabulary=[]
        for document in self.data:
            for i in range(1,len(document)):
                flag=True
                for word in self.vocabulary:
                    if word==document[i]:
                        flag=False
                        break
                if flag:   self.vocabulary.append(document[i])

    def create_dataset(self):
        self.dataset=[]
        for i in range(0,self.docnum):
            doc=self.data[i]
            self.dataset.append([])
            self.label.append(doc[0])
            for word in self.vocabulary:
                count=0
                for j in range(1,len(doc)):
                    if doc[j]==word:
                        count+=1
                self.dataset[i].append(count)

    def get_dataset(self,file):
        self.dataset=[]
        self.label=[]
        f=open(file,"r")
        count=0
        for read in f.readlines():
            self.dataset.append(read.split())
            self.label.append(self.dataset[count].pop(0))
            self.dataset[count]=map(int,self.dataset[count])
            count+=1
        self.docnum=count
        f.close()

    def get_vocabulary(self,file):
        self.vocabulary=[]
        with open(file,"r") as f:
            self.vocabulary = f.read().split()
        return self.vocabulary








