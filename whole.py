import numpy as np
from sklearn import svm
def dataset(filename):
    filehandle = open(filename,'r')
    text = filehandle.readlines()
    identity=[]
    sequences=[]
    topologies=[]
    y=[]
    dictionary={}
    A='0'
    
    for line in text:
        if line[0]=='>':
            identity.append(line.rstrip())
            print(identity)
    for line in text:
        if line[0]!= '>': 
            if line[0]!= 'M':
            	topologies.append(line.rstrip())
            	#print (topologies)
            	tops=list(topologies[0])
            	#print(tops)
            	dicttop = {'I':1, 'M':2, 'O':3}
            	#print(list(dicttop.keys()))
    for letter in tops:
    	for i in list(dicttop.keys()):
    		if letter==i:
    			y.append(dicttop.get(i))
    print (y)
    
    
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
    X=np.array(listnew)
    print(X)	    
            
    		
   #####################################################################################################################
    
    		
    		
    		
if __name__=="__main__":
    (dataset('test1'))
            
