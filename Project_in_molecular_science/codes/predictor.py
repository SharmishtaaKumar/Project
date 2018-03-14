import newsvm
import predictionparser
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
tempfile = "../datasets/test1"

savedmodel= joblib.load('firstmodel.sav')
testX=predictionparser.predictor(tempfile,31)
    

predicted=savedmodel.predict(testX)
#print(predicted)

topology_dict= {2:'I',4:'M',6:'O'}
predicted_list=predicted.tolist()
#print(predicted_list)
list_tops=[]
for number in predicted_list:
    #print(number)
	list_tops.extend(topology_dict[number])
#print(list_tops)   



##########separating the output###########
newout=0
backto=0
newlist=[]
filehandle=open(tempfile,'r')
text=filehandle.read().splitlines()
with open("predicted.txt",'w') as pr:
    for h in range(len(text)):
	    if text[h].startswith('>'):
		    pr.write(text[h])
		    pr.write("\n")
		    pr.write(text[h+1])
		    pr.write("\n")
		    newout=newout+len(text[h+1])
		    #print(newout)
		    l=''.join(list_tops[backto:newout])
		    #print(l)
		    pr.write(l)
		    pr.write("\n")
		    backto=newout
