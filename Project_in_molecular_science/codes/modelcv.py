import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
test="../datasets/test2"
def lists(filename):
    identity=[]
    sequences=[]
    topologies=[]
    for i, line in enumerate(open(filename,"r")):
        if i%3==0:
            identity.append(line.rstrip())
        elif i%3==1:
            sequences.append(line.rstrip())
        else:
            topologies.append(line.rstrip())
            
    return (identity,sequences,topologies)
def listofchar(filename):
    sequences=lists(filename)[1]
    listchars=[]
    for seqs in sequences:
        temp=[]
        for char in seqs:
            temp.append(char)
        listchars.append(temp)
    
    return(listchars)
def padding(filename,winlen):
    sequences=listofchar(filename)
    pad=(int(winlen)//2)*['0']
    #print(pad)
    finalseq=[]
    for seqs in sequences:
        #print(seqs)
        finalseq.append(pad+seqs+pad)
    return(finalseq)
def topology(filename):
    topologies = lists(filename)[2]         
    dicttop = {'I': 2, 'M': 4, 'O': 6}
    #print(list(dicttop.items()))
    new = [] 
    y=[]        
    for topo in topologies:
        list_A = []
        for z in topo:
            list_A.append(dicttop[z])
        #print(list_A)
        y.append(list_A)   
    #print(y)
    #print(len(y))
    P=np.array(y)
    return (P)
def dataset(filename,winlen):
    sequence = padding(filename,winlen)
    dictseq={}    
    a_a=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    binary= np.zeros(shape=(20,20), dtype=int)
    np.fill_diagonal(binary, 1)
    newbinary=binary.tolist()
    dictionary= zip(a_a,newbinary)
    dictseq = dict(dictionary)
    c={'0': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
    dictseq.update(c)
    finallist=[]
    for seqs in sequence:
        temp=[]
        for char in seqs:
            temp2=dictseq[char]
            temp.append(temp2)
        finallist.append(temp)
    finallist = np.array(finallist)
    
    return(finallist)
def windows(filename,winlen):
    sequence = dataset(filename,winlen)
    hey=[]
    n = (winlen-1)/2
    n = int(n)
    for seqs in sequence:
        temp=[]
        for i in range(0,len(seqs) - winlen + 1):
            newwindow=np.array(seqs[i:i+int(winlen)])
            a = newwindow.flatten()
            temp.append(a)
        hey.append(temp)
    hey = np.array(hey)
    #print(hey.shape)
    return hey
def modelinput(filename,winlen):
    seq= windows(filename,winlen)
    top=topology(filename)
    listofwindows=[]
    listoftop=[]
    for seqs in seq:
        listofwindows.extend(seqs)
    for topo in top:
        listoftop.extend(topo)
    X=np.array(listofwindows)
    Y=np.array(listoftop)
    return X,Y
def predictorinput(filename,winlen):
    identity=lists(filename)[0]
    sequence=lists(filename)[1]
    seqs=windows(filename,winlen)
    return identity, sequence, seqs
    

if __name__=="__main__":
     
    #print(dataset(test, 31))
    #windows(test, 31)
    modelinput(test, 31)
             
  
        
        
