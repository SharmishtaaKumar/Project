import numpy as np
def dataset(filename):
  
    
    filehandle = open(filename,'r')
    text = filehandle.read().splitlines()
    identity=[]
    sequences=[]
    topologies=[]
##########identity#########
    for line in text:
        if line[0]=='>':
            identity.append(line.rstrip())
    #print(identity)
    
##########topology##########
    for line in text:
        if line[0]!= '>': 
            if line[0]!= 'M':
            	topologies.append(line.rstrip())
