import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
def dataset(filename,winlen):
    filehandle = open(filename,'r')
    text = filehandle.readlines()
    identity=[]
    sequences=[]
    topologies=[]
    y=[]
    dictionary={}
    A='0'
##########identity#########
    for line in text:
        if line[0]=='>':
            identity.append(line.rstrip())
    #print(identity)
    
##########topology##########
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
    #print(y)
    #print(len(y))
    P=np.array(y)
    #print(P)
 
##########aminoacids#######
    for line in text:
        if line[0]=='M':
        	sequences.append(line.rstrip())
        	for seq in sequences:
        	    #print (sequences)
        	    seqs=''.join(sequences)
        	    #print(seqs)
        	    pad=int(winlen)//2
        	    newseq=list(seqs)
        	    #print(newseq)
        	    sequence=(pad*[A])+(newseq)+(pad*[A])
        	    #print(sequence)
        	    #print(len(sequence))
    #print(len(newseq))
        	
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
    
    
    i=iter(sequence)
    numofwin = int(len(sequence)-int(winlen)/1)+1
    hey=[]
    for i in range(0,numofwin):
    		newseq=(sequence[i:i+int(winlen)])
    		#print(newseq)
    		arr=''.join(newseq)
    		#print(arr)
    		hey.append(arr)
    #print(hey)
    listnew=[]
    seqlist=[]	
    for j in hey:
        #print(j)
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
    #print(len(listnew))
    X=np.array(listnew)
    #print(len(X))
    return X, P
    
    
#########SVM###########            
    
    
def run_svm (part1,winlen) :
       
    trainX, trainY=dataset(part1,winlen)
    #testX,testY=dataset(part2,winlen)
    #print(trainX.shape, trainY.shape, testX.shape)
    clf = svm.SVC(kernel='linear', C=1)
    clf.fit(trainX, trainY)
    #predicted=clf.predict(testX)
    #print(predicted)
    score=cross_val_score(clf, trainX, trainY, cv=3,verbose=True, n_jobs=-1)
    print(np.average(score))
    #topology_dict= {2:'I',4:'M',6:'O'}
    #predicted_list=predicted.tolist()
    #print(predicted_list)
    #list_tops=[]
    #for number in predicted_list:
       #print(number)
        #list_tops.extend(topology_dict[number])
    #new_tops=''.join(list_tops)
    #print(new_tops)
    

    
if __name__=="__main__":
    run_svm('test1','3')
    #print(dataset('test.txt'))
  
        
        
