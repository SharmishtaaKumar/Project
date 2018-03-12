import modelcv
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as rfc
def randomforest(filename):
    for n_estimators1 in (100,150,200,250,300):
        for min_samples_split_new in range(2,7):
            for winlen in range(25,36,2):
                trainX,trainY=modelcv.dataset('test',winlen)
                clf = rfc(n_estimators=n_estimators1, min_samples_split = min_samples_split_new, n_jobs=-1, class_weight='balanced')
                clf.fit(trainX, trainY)
                score=cross_val_score(clf, trainX, trainY, cv=3,verbose=True,n_jobs=-1)
                print(np.average(score),n_estimators1,min_samples_split_new,winlen)
        	
if __name__=="__main__":
    randomforest('test')
