import pssmparser
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
test = "../datasets/mydataset.txt"
def cv(filename):
    for winlen in range(25,36,2):
        for C_range in (1,5,10):
            for g_range in  (0.001,0.01):
                trainX,trainY=pssmparser.pssm_test(test,winlen)
                clf = svm.SVC(kernel='linear', C=C_range, gamma=g_range)
                clf.fit(trainX, trainY)
                score=cross_val_score(clf, trainX, trainY, cv=10,verbose=True,n_jobs=-1)
                print(np.average(score),C_range,g_range, winlen)
                
                
    return np.average(score)
    
def decisiontree(filename):
    for min_samples_split_new in range(2,7):
        for winlen in range(25,36,2):
            trainX,trainY=pssmparser.pssm_test(test,winlen)
            clf = tree.DecisionTreeClassifier(min_samples_split = min_samples_split_new,class_weight='balanced')
            clf.fit(trainX, trainY)
            score=cross_val_score(clf, trainX, trainY, cv=3,verbose=True,n_jobs=-1)
            print(np.average(score),min_samples_split_new,winlen)
            
    return np.average(score)
    
def randomforest(filename):
    for n_estimators1 in (100,150,200,250,300):
        for min_samples_split_new in range(2,7):
            for winlen in range(25,36,2):
                trainX,trainY=modelcv.dataset(test,winlen)
                clf = rfc(n_estimators=n_estimators1, min_samples_split = min_samples_split_new, n_jobs=-1, class_weight='balanced')
                clf.fit(trainX, trainY)
                score=cross_val_score(clf, trainX, trainY, cv=3,verbose=True,n_jobs=-1)
                print(np.average(score),n_estimators1,min_samples_split_new,winlen)
                
    return np.average(score)
    
if __name__=="__main__":
    cv('mydataset.txt')
    decisiontree('mydataset.txt')
    randomforest('mydataset.txt')
