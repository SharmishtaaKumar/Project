import modelcv
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.externals import joblib
test = "../datasets/test"

def randomforest(filename):
    trainX,trainY=modelcv.dataset(test,29)
    clf = rfc(n_estimators=250, min_samples_split =6, n_jobs=-1, class_weight='balanced')
    clf.fit(trainX, trainY)
    score=cross_val_score(clf, trainX, trainY, cv=3,verbose=True,n_jobs=-1)
    print(np.average(score))
    inputfile='rfcmodel.sav'
    joblib.dump(clf,inputfile)
        	
if __name__=="__main__":
    #print(dataset(test,'29'))
    randomforest('test')
