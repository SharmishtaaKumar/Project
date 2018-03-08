import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
import dataset as ds
def run_svm (part1,part2,winlen) :   
    trainX, trainY=ds(part1,winlen)
    testX,testY=ds(part2,winlen)
    print(trainX.shape, trainY.shape, testX.shape)
    clf = svm.SVC(kernel='linear', C=1)
    clf.fit(trainX, trainY)
    predicted=clf.predict(testX)
    #print(predicted)
    
    topology_dict= {2:'I',4:'M',6:'O'}
    predicted_list=predicted.tolist()
    #print(predicted_list)
    list_tops=[]
    for number in predicted_list:
       #print(number)
        list_tops.extend(topology_dict[number])
    new_tops=''.join(list_tops)
    print(new_tops)
if __name__=="__main__":
    run_svm('test', 'test1','3')
