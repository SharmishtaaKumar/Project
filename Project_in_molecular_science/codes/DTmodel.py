import modelcv
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import tree
from sklearn.externals import joblib
test = "../datasets/test"
def decisiontree(filename):
    trainX,trainY=modelcv.dataset(test,33)
    clf = tree.DecisionTreeClassifier(min_samples_split = 5,class_weight='balanced')
    clf.fit(trainX, trainY)
    score=cross_val_score(clf, trainX, trainY, cv=3,verbose=True,n_jobs=-1)
    print(np.average(score))
    inputfile='dtmodel.sav'
    joblib.dump(clf,inputfile)
          
if __name__=="__main__":
    decisiontree('test')
