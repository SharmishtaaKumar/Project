
import numpy as np
from sklearn import svm
from itertools import chain
from sklearn.externals import joblib
from pathlib import Path

tempfile="../datasets/pssm_test"

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
		myfile=Path('../fastaoutput/' + (str(name) + '.fasta.pssm'))
		if myfile.is_file():
			pssm_array=(np.genfromtxt('../fastaoutput/' + (str(name) + '.fasta.pssm'), skip_header = 3, skip_footer = 5,  usecols = range(22,42), autostrip = True))/100
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
	newarray=np.array(newlist)
	#print(newarray.shape)
	return newarray
def predictor(filename,winlen):
	identity= lists(filename)[0]
	sequences=lists(filename)[1]
	seqs= pssm_test(filename,winlen)
	savedmodel= joblib.load('../models/PSSM_SVC_model.sav')
	topology_dict= {2:'I',4:'M',6:'O'}
	temp=savedmodel.predict(seqs)
	#print(temp)
	newpred=[]
	predictions=[]
	for j in range(len(temp)):
		newpred.extend(topology_dict[temp[j]])   
	string=''.join(newpred)
	predictions.append(string)
	with open("../Predicted texts/PSSM_SVC_results",'w') as pr:
		for i in range(len(identity)):
			pr.write(identity[i]+ "\n" + sequences[i]+ "\n" + predictions[i] + "\n")
if __name__=="__main__":
	lists(tempfile)
	pssm_test(tempfile,31)
	#formatpssm(tempfile,31)
	#topology(tempfile,31)
	predictor(tempfile, 31)
           
