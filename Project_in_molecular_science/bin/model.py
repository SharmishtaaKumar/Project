import dataset
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
def run_svm (part1,part2) :   
    trainX, trainY=dataset(part1)
    testX,testY=dataset(part2)
    #print(trainX.shape, trainY.shape, testX.shape)
    clf = svm.SVC(kernel='linear', C=1)
    clf.fit(trainX, trainY)
    predicted=clf.predict(testX)
   #print(predicted)
    topology_dict= {'I': 2, 'M': 4, 'O': 6}
    predicted_list=predicted.tolist()
   #print(predicted_list)
    list_tops=[]
    for number in predicted_list:
        print(number)
        list_tops.extend(topology_dict[number])
    print(list_tops)
    

    
if __name__=="__main__":
    run_svm('test', 'test1')
