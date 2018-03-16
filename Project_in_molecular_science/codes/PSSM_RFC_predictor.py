import pssmparser
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.metrics import matthews_corrcoef
from sklearn.externals import joblib 
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
tempfile="../datasets/50unknownproteins"

####VALIDATING RESULTS###########
savedmodel= joblib.load('../models/PSSM_RFC_model.sav')
testX,testY=pssmparser.pssm_test(tempfile,33)
predictedY=savedmodel.predict(testX)
print(matthews_corrcoef(testY, predictedY))   
print(accuracy_score(testY, predictedY))
confusionmat = confusion_matrix(testY, predictedY)
confusion_norm=preprocessing.normalize(confusionmat)
states = ['I:Insideofthemembrane', 'M:Transmembraneregion', 'O:Outsideofthemembrane']
print(classification_report(testY, predictedY, target_names=states))
confusionmat = confusion_matrix(testY, predictedY)
confusion_norm=preprocessing.normalize(confusionmat)
states = ['I:Insideofthemembrane', 'M:Transmembraneregion', 'O:Outsideofthemembrane']
print(classification_report(testY, predictedY, target_names=states))


########TO GET NECESSARY OUTPUT##########
topology_dict= {2:'I',4:'M',6:'O'}
predicted_list=predictedY.tolist()
#print(predicted_list)
list_tops=[]
for number in predicted_list:
    #print(number)
	list_tops.extend(topology_dict[number])
#print(list_tops)   

newout=0
backto=0
newlist=[]
filehandle=open(tempfile,'r')
text=filehandle.read().splitlines()
with open("../Predicted texts/PSSM_RFC_predicted.txt",'w') as pr:
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
