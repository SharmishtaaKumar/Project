import svm_new
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
def cv(filename):
    for winlen in range (31,34,2):
        trainX,trainY=svm_new.dataset('test',winlen)
        clf = svm.SVC(kernel='linear', C=1)
        clf.fit(trainX, trainY)
        score=cross_val_score(clf, trainX, trainY, cv=10,verbose=True,n_jobs=-1)
        print(np.average(score))
if __name__=="__main__":
    cv('test')
