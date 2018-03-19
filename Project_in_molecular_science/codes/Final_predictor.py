import modelcv
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
tempfile = "../datasets/50unknownproteins"

#### VALIDATING RESULTS FOR SVC ###########
savedmodel= joblib.load('../models/firstmodel_SVC.sav')
testX,testY=modelcv.dataset(tempfile,31)
predictedY=savedmodel.predict(testX)
with open("../Predicted texts/SVC_scores_final50.txt",'w') as pr:
    pr.write("The MCC score is")
    pr.write(str(matthews_corrcoef(testY, predictedY)))
    pr.write("\n")
    pr.write("The accuracy sscore is ")
    pr.write(str(accuracy_score(testY, predictedY)))
    pr.write("\n")
    pr.write("The confusion matrix is as follows ")
    pr.write("\n")
    confusionmat = confusion_matrix(testY, predictedY)
    pr.write(str(confusionmat))
    pr.write("\n")
    states = ['I:Insideofthemembrane', 'M:Transmembraneregion', 'O:Outsideofthemembrane']
    pr.write("The classification report is as follows")
    pr.write(str(classification_report(testY, predictedY, target_names=states)))
    pr.write("\n")
pr.close()


######## TO GET NECESSARY OUTPUT ##########
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
with open("../Predicted texts/SVC_predicted_final50.txt",'w') as pr:
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
		    
##### VALIDATING RESULTS FOR PSSM_SVC #########

savedmodel= joblib.load('../models/PSSM_SVC_model.sav')
testX,testY=pssmparser.pssm_test(tempfile,31)
predictedY=savedmodel.predict(testX)
with open("../Predicted texts/PSSM_SVC_scores_final50.txt",'w') as pr:
    pr.write("The MCC score is ")
    pr.write(str(matthews_corrcoef(testY, predictedY)))
    pr.write("\n")
    pr.write("The accuracy sscore is ")
    pr.write(str(accuracy_score(testY, predictedY)))
    pr.write("\n")
    pr.write("The confusion matrix is as follows ")
    pr.write("\n")
    confusionmat = confusion_matrix(testY, predictedY)
    pr.write(str(confusionmat))
    pr.write("\n")
    states = ['I:Insideofthemembrane', 'M:Transmembraneregion', 'O:Outsideofthemembrane']
    pr.write("The classification report is as follows")
    pr.write(str(classification_report(testY, predictedY, target_names=states)))
    pr.write("\n")
pr.close()

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
with open("../Predicted texts/PSSM_SVC_predicted_final50.txt",'w') as pr:
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
