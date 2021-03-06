import dictionary
import numpy as np
from sklearn import svm
from itertools import chain
from sklearn.externals import joblib
from pathlib import Path

tempfile="../datasets/pssm_train"

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
    #print (len(sequences))        
    return (identity,sequences,topologies)

def pssm_test(filename,winlen):
	identity= lists(filename)[0]
	newlist=[]
	newarray=[]
	top=[]
	for name in identity:
		#print(name)
		myfile=Path('../fasta_data/' + (str(name) + '.fasta.pssm'))
		if myfile.is_file():
			
			pssm_array=(np.genfromtxt('../fasta_data/' + (str(name) + '.fasta.pssm'), skip_header = 3, skip_footer = 5,  usecols = range(22,42), autostrip = True))/100
			pssm_array=pssm_array.tolist()
			#print(len(pssm_array))
			pssm_array=list(chain(*pssm_array))
			add_windows=[0]*(20*int(winlen/2))
			pssm_array=add_windows+pssm_array+add_windows
			#print(pssm_array)
			listofarrays=[]
			for x in range (0,len(pssm_array),20):
				window=pssm_array[x:x+winlen*20]
				if len(window)==winlen*20:
				
					listofarrays.append(window)
			newlist.extend(listofarrays)
	
	#print(len(newlist))
	return newlist
def topology(filename,winlen):
    topologies = lists(filename)[2]
    #print(topologies)      
    dicttop = {'I': 2, 'M': 4, 'O': 6}
    #print(list(dicttop.items()))
    y=[]        
    for topo in topologies:
        list_A = []
        for z in topo:
            list_A.append(dicttop[z])
        #print(list_A)
        y.extend(list_A)   
    #print(y)
    #print(len(y))
    return (y)
def modelinput(filename,winlen):
    seq= pssm_test(filename,winlen)
    top=topology(filename,winlen)
    X=np.array(seq)
    Y=np.array(top)
    #print(X.shape,Y.shape)
    
    return X,Y
    

if __name__=="__main__":
	lists(tempfile)
	pssm_test(tempfile,31)
	#formatpssm(tempfile,31)
	topology(tempfile,31)
	modelinput(tempfile, 31)
           
                
                
               
        
