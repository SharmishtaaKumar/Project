import dictionary
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib
from sklearn.metrics import matthews_corrcoef
from pathlib import Path
from sklearn.metrics import confusion_matrix
tempfile="../datasets/test"

#dictionary = dictionary.dataset(tempfile)
def pssm_test(filename,winlen):
    dictionary_pssm = dictionary.dataset(filename)
    #print(dictionary.keys())
    listofkeys=[]
    listofarrays=[]
    listoftop=[]
    #for newkey in dictionary.keys():
    #    print(newkey)
    #    newnames= str(newkey) + '.fasta.pssm'
    #    listofkeys.append(newnames)
    #print(listofkeys)

    for name in dictionary_pssm.keys():
        #print(name)
        myfile=Path('../fasta_data/' + (str(name) + '.fasta.pssm'))
        if myfile.is_file():
        
            #print(name)
            pssm_array=(np.genfromtxt('../fasta_data/' + (str(name) + '.fasta.pssm'), skip_header = 3, skip_footer = 5,  usecols = range(22,42), autostrip = True))/100
            listofarrays.append(pssm_array)
            listoftop.append(dictionary_pssm[name][1])
            #print(name)
    #print(listoftop)    
    #print(listofarrays)
    
#####sliding windows#######
    main_list = []
    pad = int(winlen)//2
    zero_array = np.zeros(20, dtype=int)    
    for new_element in listofarrays:
        win_list = []
        for element in range(0, len(new_element)):
            temp =[]
            if element <= 0:
                seq_window = new_element[(element):(element+pad+1)]
                diff = int(winlen)-len(seq_window)
                for i in range(0, diff):
                    temp.append(zero_array)
                temp.extend(seq_window)   
            elif element > 0 and element < pad: 
                seq_window = new_element[0:(element+pad+1)]
                difference = int(winlen)-len(seq_window)
                for i in range(0, difference):
                    temp.append(zero_array)
                temp.extend(seq_window)   
            elif element >= pad:
                seq_window3 = new_element[(element-pad):(element+pad+1)]
                if len(seq_window) == int(winlen):  
                    temp.extend(seq_window)    
                if len(seq_window) < int(winlen): 
                    difference = int(winlen)-len(seq_window)
                    temp.extend(seq_window)
                    for i in range(0, difference):
                        temp.append(zero_array)
            temp= np.array(temp)
            final_window = temp.flatten()
            win_list.append(final_window)
        main_list.extend(win_list)
    templist = np.array(main_list)
    #print(len(templist))
####for topology######
    dicttop = {'I': 2, 'M': 4, 'O': 6}
    #print(list(dicttop.items()))
    new = [] 
    y=[]        
    for topo in listoftop:
        list_A = []
        for z in topo:
            list_A.append(dicttop[z])
        #print(list_A)
        y.extend(list_A)   
    #print(y)
    #print(len(y))
    labels=np.array(y)
    #print(len(labels))
    return templist, labels
    
if __name__=="__main__":
    pssm_test(tempfile,'31')        
                
                
                
               
        
