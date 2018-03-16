import pssmparser
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier as rfc

test = "../datasets/test"
def cv(filename):
    trainX,trainY=pssmparser.pssm_test(test,31)
    clf = svm.SVC(kernel='linear', C=1, gamma=0.01)
    clf.fit(trainX, trainY)
    inputfile='PSSM_SVC_model.sav'
    joblib.dump(clf,inputfile,compress=9)
    
def decisiontree(filename):
    trainX,trainY=pssmparser.pssm_test(test,29)
    clf = tree.DecisionTreeClassifier(min_samples_split=6,class_weight='balanced')
    clf.fit(trainX, trainY)
    inputfile='PSSM_DT_model.sav'
    joblib.dump(clf,inputfile,compress=9)
    
def randomforest(filename):
    trainX,trainY=pssmparser.pssm_test(test,33)
    clf = rfc(n_estimators=100, min_samples_split = 6, n_jobs=-1, class_weight='balanced')
    clf.fit(trainX, trainY)
    inputfile='PSSM_RF_model.sav'
    joblib.dump(clf,inputfile,compress=9)
              
            
if __name__=="__main__":
    cv('test')
    decisiontree('test')
    randomforest('test')
