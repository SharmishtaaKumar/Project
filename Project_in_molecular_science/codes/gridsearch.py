import newsvm
import pandas as pd
import numpy as np
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import KFold
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import make_scorer
from sklearn.metrics import f1_score
from sklearn.externals import joblib
test = "../datasets/test"
def cv(filename, winlen):
    trainX,trainY=newsvm.dataset(test,winlen)
    C_values=[1,5,10]
    g_values=[0.001,0.01]
        
    param={'C' : C_values, 'gamma' : g_values}
    clf = GridSearchCV(SVC(), param, n_jobs=1, cv=3, verbose=True, error_score=np.NaN, return_train_score=False)
    #clf = svm.SVC(kernel='linear', C=1)
    clf.fit(trainX, trainY)
    df=pd.DataFrame(clf.cv_results_)
    #print(newscores)
    filename = '../Datasets/' + str(winlen) + '_improved' + '.csv'
    df.to_csv(filename, sep='\t', encoding='UTF-8')

        
        #score=cross_val_score(clf, trainX, trainY, cv=10,verbose=True,n_jobs=-1)
        #print(np.average(score))
if __name__=="__main__":
    cv('test','31')
