import numpy as np
import dictionary
import pssmparser
def slide_win(winlen):
    pssmarray=pssmparser.formatpssm('>A2RI47|4popA.fasta.pssm')
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
            print(temp_window)
        
        
        
    
if __name__=="__main__":
    slide_win(3)
