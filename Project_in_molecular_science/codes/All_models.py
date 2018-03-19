import modelcv
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.externals import joblib
test = "../datasets/test"
def run_svm (filename) :   
    trainX,trainY=modelcv.dataset(test,31)
    clf = svm.SVC(kernel='linear',C=1, gamma=0.01)
    clf.fit(trainX, trainY)
    inputfile='../models/firstmodel_SVC.sav'
    joblib.dump(clf,inputfile)
def decisiontree(filename):
    trainX,trainY=modelcv.dataset(test,33)
    clf = tree.DecisionTreeClassifier(min_samples_split = 5,class_weight='balanced')
    clf.fit(trainX, trainY)
    #score=cross_val_score(clf, trainX, trainY, cv=3,verbose=True,n_jobs=-1)
    #print(np.average(score))
    inputfile='../models/DTmodel.sav'
    joblib.dump(clf,inputfile)
def randomforest(filename):
    trainX,trainY=modelcv.dataset(test,33)
    clf = rfc(n_estimators=250, min_samples_split =6, n_jobs=-1, class_weight='balanced')
    clf.fit(trainX, trainY)
    #score=cross_val_score(clf, trainX, trainY, cv=3,verbose=True,n_jobs=-1)
    #print(np.average(score))
    inputfile='../models/RFCmodel.sav'
    joblib.dump(clf,inputfile,compress=9)
          
if __name__=="__main__":
    run_svm('test')
    decisiontree('test')
    randomforest('test')
