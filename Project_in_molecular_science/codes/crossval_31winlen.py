import modelcv
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
test = "../datasets/test"
def cv(filename):
    for C_range in (1,5,10):
        for g_range in  (0.001,0.01):
            trainX,trainY=modelcv.dataset(test,31)
            clf = svm.SVC(kernel='linear', C=C_range, gamma=g_range)
            clf.fit(trainX, trainY)
            score=cross_val_score(clf, trainX, trainY, cv=10,verbose=True,n_jobs=-1)
            print(np.average(score),C_range,g_range)
if __name__=="__main__":
    cv('test')
