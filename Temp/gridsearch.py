import modelcv
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

def cv(filename):
    for winlen in range (29,32,2):
      
        trainX,trainY=modelcv.dataset('test',winlen)
        C_values=[1,5,10]
        g_values=[0.001,0.01]
        
        param={'C' : C_values, 'gamma' : g_values}
        clf = GridSearchCV(SVC(), param, n_jobs=1, cv=3, verbose=True, error_score=np.NaN, return_train_score=False)
        #clf = svm.SVC(kernel='linear', C=1)
        clf.fit(trainX, trainY)
        newscores=pd.Dataframe(clf.cv_results)
        print(newscores)
        filename = '../Datasets/' + str(windowsize) + '_improved' + '.csv'
        df.to_csv(filename, sep='\t', encoding='UTF-8')

        
        #score=cross_val_score(clf, trainX, trainY, cv=10,verbose=True,n_jobs=-1)
        #print(np.average(score))
if __name__=="__main__":
    cv('test')
