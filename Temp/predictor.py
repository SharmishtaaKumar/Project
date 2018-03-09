import newsvm
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib


trainX,trainY=newsvm.dataset('test')
testX=newsvm.predictor('test1')
    
clf = svm.SVC(kernel='linear', C=1)
clf.fit(trainX, trainY)
predicted=clf.predict(testX)
#print(predicted)

topology_dict= {2:'I',4:'M',6:'O'}
predicted_list=predicted.tolist()
#print(predicted_list)
list_tops=[]
for number in predicted_list:
    #print(number)
	list_tops.extend(topology_dict[number])
new_tops=list_tops
print(list_tops)   

newout=0
backto=0
newlist=[]
filehandle=open('test1','r')
text=filehandle.read().splitlines()
for h in range(len(text)):
	if text[h].startswith('>'):
		print(text[h])
		print(text[h+1])
		newout=newout+len(text[h+1])
		print(newout)
		l=''.join(list_tops[backto:newout])
		print(l)
		backto=newout
