tempfile="../datasets/mydataset.txt"

import pssmparser
import numpy as np
def slidingwin(pssmarray,winlen):                         
   
    pssm_new=[]
    wins= int(winlen)//2
    for i in range(len(pssmarray)):
        #print (i)
        if i < wins:
            numofwin = wins-i
            window = [0]*(20*numofwin)
            for newlist in pssmarray[:i+wins+1]:
                #print (lists) works
                window.extend(newlist)  
            pssm_new.append(window) 

        elif i > (len(pssmarray)-wins-1):
            #print(i)
            numofwin = wins - (len(pssmarray)- 1 - i)
            window = []
            for newlist in pssmarray[i-wins:]:
                window.extend(newlist)  # Extend (not append)
            window.extend([0]*(20*numofwin))
            pssm_new.append(window) # Save to pssm training set

        else:
            temp_window = pssmarray[i-wins:i+wins+1]
            #print(temp_window)
            window=[]
            for newlist in temp_window:
                window.extend(newlist)
            pssm_new.append(window)
             
            
    print( pssm_new)
    
    
