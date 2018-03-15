import dictionary
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
from pathlib import Path
tempfile="../datasets/50proteinstobepredicted"

dictionary = dictionary.dataset(tempfile)
def pssm_test(filename,winlen):
    #dictionary = dictionary.dataset(tempfile)
    #print(dictionary.keys())
    listofkeys=[]
    listofarrays=[]
    listoftop=[]
    #for newkey in dictionary.keys():
    #    print(newkey)
    #    newnames= str(newkey) + '.fasta.pssm'
    #    listofkeys.append(newnames)
    #print(listofkeys)

    for name in dictionary.keys():
        #print(name)
        myfile=Path('../50fastadata/' + (str(name) + '.fasta.pssm'))
        if myfile.is_file():
        
            #print(name)
            pssm_array=(np.genfromtxt('../50fastadata/' + (str(name) + '.fasta.pssm'), skip_header = 3, skip_footer = 5,  usecols = range(22,42), autostrip = True))/100
            listofarrays.append(pssm_array)
            listoftop.append(dictionary[name][1])
            #print(name)
    #print(listoftop)    
    #print(listofarrays)


    main_list = []
    pad = int(winlen)//2
    zero = np.zeros(20, dtype=int)
    
    for element in listofarrays:
        win_list = []
        for array in range(0, len(element)):
            temp_window =[]
            if array <= 0:
                seq_window = element[(array):(array+pad+1)]
                diff = int(winlen)-len(seq_window)
                for i in range(0, diff):
                    temp_window.append(zero)
                temp_window.extend(seq_window)   
            elif array > 0 and array < pad: 
                seq_window = element[0:(array+pad+1)]
                diff = int(winlen)-len(seq_window)
                for i in range(0, diff):
                    temp_window.append(zero)
                temp_window.extend(seq_window)   
            elif array >= pad:
                seq_window3 = element[(array-pad):(array+pad+1)]
                if len(seq_window) == int(winlen):  
                    temp_window.extend(seq_window)    
                if len(seq_window) < int(winlen): 
                    diff = int(winlen)-len(seq_window)
                    temp_window.extend(seq_window)
                    for i in range(0, diff):
                        temp_window.append(zero)
            temp_window = np.array(temp_window)
            final_window = temp_window.flatten()
            win_list.append(final_window)
        main_list.extend(win_list)
    templist = np.array(main_list)
    #print(len(templist))
    
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
    
    
    
    
    
