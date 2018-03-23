import modelcv
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
filename = "../datasets/50unknownproteins"
topology_dict= {2:'I',4:'M',6:'O'}
identity, sequence, seqs = modelcv.predictorinput(filename,31)
savedmodel= joblib.load('../models/firstmodel_SVC.sav')
predictions=[]
for i in range(len(seqs)):
    temp=savedmodel.predict(seqs[i])
    newpred=[]
    for j in range(len(temp)):
        newpred.extend(topology_dict[temp[j]])   
    string=''.join(newpred)
    predictions.append(string)
with open("../Predicted texts/RFCpredicted.txt",'w') as pr:
    for i in range(len(identity)):
        pr.write(identity[i]+ "\n" + sequence[i]+ "\n" + predictions[i] + "\n")

