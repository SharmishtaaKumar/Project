import pssmparser
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier as rfc

test = "../datasets/pssm_train"
def cv(filename):
    for winlen in range(25,36,2):
        for C_range in (1,5,10):
            for g_range in  (0.001,0.01):
                trainX,trainY=pssmparser.modelinput(test,winlen)
                clf = svm.SVC(kernel='linear', C=C_range, gamma=g_range)
                clf.fit(trainX, trainY)
                score=cross_val_score(clf, trainX, trainY, cv=10,verbose=True,n_jobs=-1)
                print(np.average(score),C_range,g_range, winlen)
                
              
    
if __name__=="__main__":
    cv(test)
    
