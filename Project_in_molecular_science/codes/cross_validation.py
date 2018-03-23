import modelcv
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
test = "../datasets/test"
def cv(filename):
    for winlen in range (31,36,2):
        for cv_new in (3,5,10):
      
            trainX,trainY=modelcv.modelinput(test,winlen)
            clf = svm.SVC(kernel='linear', C=1)
            clf.fit(trainX, trainY)
            score=cross_val_score(clf, trainX, trainY, cv=cv_new,verbose=True,n_jobs=-1)
            print(np.average(score),winlen,cv_new)
if __name__=="__main__":
    cv('test')
