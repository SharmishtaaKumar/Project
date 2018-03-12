import modelcv
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score

def cv(filename):
    for winlen in range (3,32,2):
      
        trainX,trainY=modelcv.dataset('test',winlen)
        clf = svm.SVC(kernel='linear', C=1)
        clf.fit(trainX, trainY)
        score=cross_val_score(clf, trainX, trainY, cv=10,verbose=True,n_jobs=-1)
        print(np.average(score))
if __name__=="__main__":
    cv('test')