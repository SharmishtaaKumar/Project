import numpy as np
from sklearn import svm
def dataset(filename):
    filehandle = open(filename,'r')
    text = filehandle.readlines()
    identity=[]
    sequences=[]
    topologies=[]
    o=[]
    dictionary={}
    A='0'
##########identity
    for line in text:
        if line[0]=='>':
            identity.append(line.rstrip())
    #print(identity)
    
##########topology
    for line in text:
        if line[0]!= '>': 
            if line[0]!= 'M':
            	topologies.append(line.rstrip())
    #print (topologies)    	
    dicttop = {'I': 1, 'M': 2, 'O': 3}
    #print(list(dicttop.items()))
    new = [] 
    y=[]        
    for topo in topologies:
        list_A = []
        for z in topo:
            list_A.append(dicttop[z])
        #print(list_A)
    o.extend(list_A)
    y=np.array(o)
    #print(y)
 
##########aminoacids
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
    #print(X)	    
    return X, y
####SVM####            
    
    #clf = svm.SVC()
    #clf.fit(X, y)
    #print(clf.predict(X))
def try_stuff (part1,part2) :   
    trainX, trainY=dataset(part1)
    print(trainX.shape,trainY.shape)
    testX,testY=dataset(part2)
    print(testX.shape)
    clf = svm.SVC()
    clf.fit(trainX, trainY)
    print(clf.predict(testX))
    
    
    
    
    
if __name__=="__main__":
    try_stuff('test', 'test1')
            