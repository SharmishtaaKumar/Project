import pssmparser
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from pathlib import Path
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.externals import joblib

test = "../datasets/pssm_train"
def SVC_run(filename):
    trainX,trainY=pssmparser.modelinput(test,31)
    clf = svm.SVC(kernel='linear', C=1, gamma=0.01,class_weight='balanced')
    clf.fit(trainX, trainY)
    inputfile='../models/PSSM_SVC_model.sav'
    joblib.dump(clf,inputfile,compress=9)
                   
if __name__=="__main__":
    SVC_run(test)

