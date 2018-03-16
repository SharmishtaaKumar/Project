import pssmparser
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from pathlib import Path
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.externals import joblib

test = "../datasets/test"
def SVC_run(filename):
    trainX,trainY=pssmparser.pssm_test(test,31)
    clf = svm.SVC(kernel='linear', C=1, gamma=0.01)
    clf.fit(trainX, trainY)
    inputfile='../models/PSSM_SVC_model.sav'
    joblib.dump(clf,inputfile,compress=9)
    
def decisiontree(filename):
    trainX,trainY=pssmparser.pssm_test(test,29)
    clf = tree.DecisionTreeClassifier(min_samples_split=6,class_weight='balanced')
    clf.fit(trainX, trainY)
    inputfile='../models/PSSM_DT_model.sav'
    joblib.dump(clf,inputfile,compress=9)
    
def randomforest(filename):
    trainX,trainY=pssmparser.pssm_test(test,33)
    clf = rfc(n_estimators=100, min_samples_split = 6, n_jobs=-1, class_weight='balanced')
    clf.fit(trainX, trainY)
    inputfile='../models/PSSM_RFC_model.sav'
    joblib.dump(clf,inputfile,compress=9)
              
            
if __name__=="__main__":
    SVC_run('test')
    decisiontree('test')
    randomforest('test')
