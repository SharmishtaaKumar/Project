import modelcv
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn import tree
def decisiontree(filename):
    for min_samples_split_new in range(2,7):
        for winlen in range(25,36,2):
            trainX,trainY=modelcv.dataset('test',winlen)
            clf = tree.DecisionTreeClassifier(min_samples_split = min_samples_split_new,class_weight='balanced')
            clf.fit(trainX, trainY)
            score=cross_val_score(clf, trainX, trainY, cv=3,verbose=True,n_jobs=-1)
            print(np.average(score),min_samples_split_new,winlen)
            #tree.export_graphviz(clf,out_file='decisiontree.dot')
if __name__=="__main__":
    decisiontree('test')
