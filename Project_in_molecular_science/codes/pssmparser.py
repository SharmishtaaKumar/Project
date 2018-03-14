tempfile="../datasets/mydataset.txt"

import pssmtry
import numpy as np
from pathlib import Path
winlen=3
dictionary = pssmtry.fasta(tempfile)
#print(dictionary.keys())
listofkeys=[]
listofarrays=[]
for newkey in dictionary.keys():
    newnames= str(newkey) + '.fasta.pssm'
    listofkeys.append(newnames)
#print(listofkeys)

for name in listofkeys:
    myfile=Path('../PSSM/fasta_data/' + name)
    if myfile.is_file():
        #print(name)
        pssm_array=(np.genfromtxt('../PSSM/fasta_data/' + name, skip_header = 3, skip_footer = 5, usecols = range(22,42), autostrip = True))/100
        listofarrays.append(pssm_array)
#print(listofarrays)

for newarray in listofarrays:
    #print(newarray)
    allpssmlist=[]
    pssm_new=[]
    wins= int(winlen)//2
    for seq in newarray:
        multilist=[]
        for i in range(0,len(seq)):
        #print (i)
            if i < wins:
                numofwin = wins-i
                window = [0]*(20*numofwin)
                for newlist in seq[:i+wins+1]:
                    #print (lists) works
                    window.extend(newlist)  
                pssm_new.append(window) 

            elif i > (len(seq)-wins-1):
                #print(i)
                numofwin = wins - (len(seq)- 1 - i)
                window = []
                for newlist in seq[i-wins:]:
                    window.extend(newlist)  
                window.extend([0]*(20*numofwin))
                pssm_new.append(window) 

            else:
                temp_window = seq[i-wins:i+wins+1]
                window = []
                for newlist in temp_window:
                    window.extend(newlist)
                pssm_new.append(window)
        pssmnewarray=np.array(pssm_new)
        print(len(pssmnewarray)) 


                
                
                
                
               
        
