import svm_new
import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib


    
    topology_dict= {2:'I',4:'M',6:'O'}
    predicted_list=predicted.tolist()
    #print(predicted_list)
    list_tops=[]
    for number in predicted_list:
       #print(number)
       list_tops.extend(topology_dict[number])
    #new_tops=list_tops
    return list_tops
    x=
    newout=0
    backto=0
    for h in range(len(part2)):
        print(h)
        if part2[h].startswith (">"):
            print(part2)
            return (part2[0])
            return (part2[1])
            newout=newout+len(part2[h+1])
            l="".join(list_tops[backto:newout])
            return (l)
            backto=newout
