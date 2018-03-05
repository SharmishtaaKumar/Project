import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
def dataset(filename):
    filehandle = open(filename,'r')
    text = filehandle.readlines()
    identity=[]
    sequences=[]
    topologies=[]
    y=[]
    dictionary={}
    A='0'
<<<<<<< HEAD
##########identity#########
=======
##########identity
>>>>>>> 60b3c0b94a493c3bcd4aa7e7a446919bb9186587
    for line in text:
        if line[0]=='>':
            identity.append(line.rstrip())
    #print(identity)
    
<<<<<<< HEAD
##########topology##########
=======
##########topology
>>>>>>> 60b3c0b94a493c3bcd4aa7e7a446919bb9186587
    for line in text:
        if line[0]!= '>': 
            if line[0]!= 'M':
            	topologies.append(line.rstrip())
    #print (topologies)    	
    dicttop = {'I': 2, 'M': 4, 'O': 6}
    #print(list(dicttop.items()))
    new = [] 
    y=[]        
    for topo in topologies:
        list_A = []
        for z in topo:
            list_A.append(dicttop[z])
        #print(list_A)
    y.extend(list_A)
    O=np.array(y)
    #print(len(O))
 
<<<<<<< HEAD
##########aminoacids#######
=======
##########aminoacids
>>>>>>> 60b3c0b94a493c3bcd4aa7e7a446919bb9186587
    for line in text:
        if line[0]=='M':
        	sequences.append(line.rstrip())
        	for seq in sequences:
        	    #print (sequences)
        	    seqs=[A]+list(seq)+[A]
        	    #print(seqs)
        	
    dictseq={}    
    a_a=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    #print (a_a)
    binary= np.zeros(shape=(20,20), dtype=int)
    np.fill_diagonal(binary, 1)
    #print (binary)
    newbinary=binary.tolist()
    dictionary= zip(a_a,newbinary)
    dictseq = dict(dictionary)
    c={'0': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    dictseq.update(c)
    #print (c)
    #print (dictseq)
    
    
    i=iter(seqs)
    numofwin = int(len(seqs)-3/1)+1
    hey=[]
    for i in range(0,numofwin):
    		newseq=(seqs[i:i+3])
    		#print(newseq)
    		arr=''.join(newseq)
    		#print(arr)
    		hey.append(arr)
    #print(hey)
    listnew=[]
    seqlist=[]	
    for j in hey:
        newlist=[]
        for k in j:
            for key,value in dictseq.items():
                #print(value)
                if k==key:
                    newlist.extend(value)
                    #print(newlist)
        seqlist.append(newlist)
        #print(seqlist)
    listnew=seqlist
    #print (listnew)
    X=np.array(listnew)
    #print(len(X))	    
    return X, O
<<<<<<< HEAD
    
    
#########SVM###########            
    
    
def run_svm (part1,part2) :   
    trainX, trainY=dataset(part1)
    testX,testY=dataset(part2)
    #print(trainX.shape, trainY.shape, testX.shape)
    clf = svm.SVC(kernel='linear', C=1)
    clf.fit(trainX, trainY)
=======
    ####SVM####            
    
    #clf = svm.SVC()
    #clf.fit(X, o)
    #print(clf.predict(X))
def run_svm (part1,part2) :   
    trainX, trainY=dataset(part1)
    testX,testY=dataset(part2)
    print(trainX.shape, trainY.shape, testX.shape)
    clf = svm.SVC()
    clf.fit(trainX, trainY)
    print(clf.predict(testX))
    
    
    
>>>>>>> 60b3c0b94a493c3bcd4aa7e7a446919bb9186587
    
    predicted=clf.predict(testX)
    #print(predicted)
    topology_dict={'I': 2, 'M': 4, 'O': 6}
    predicted_new=predicted.tolist()
    #print(predicted_new)
    predicted_tops=[]
    for number in predicted_new:
        #print(number)
        predicted_tops.extend(topology_dict[number])
    print(predicted_tops)
 
    
if __name__=="__main__":
<<<<<<< HEAD
    run_svm('test', 'test1')
    #print(dataset('test.txt'))
=======
    run_svm('test.txt', 'test1.txt')
    #print(dataset('test.txt'))
        
        
>>>>>>> 60b3c0b94a493c3bcd4aa7e7a446919bb9186587
