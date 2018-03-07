import numpy as np
def parser(file_name):
    filehandle = open(file_name,'r')
    text = filehandle.readlines()
    sequences=[]
    topologies=[]
    for line in text:
        if line[0]!= '>': 
            if line[0]!= 'M':
            	topologies.append(line.rstrip())
    #print (topologies)    	
    dicttop = {'I': 2, 'M': 4, 'O': 6}
    #print(list(dicttop.items()))
    new = [] 
    y=[]        
    for topo in topologies:
        list_A = []
        for z in topo:
            list_A.append(dicttop[z])
        #print(list_A)
        y.extend(list_A)   
    print(y)
    #print(len(y))
    P=np.array(y)
    #print(P)
    for line in text:
        if line[0]=='M':
        	sequences.append(line.rstrip())
        	for seq in sequences:
        	    #print (sequences)
        	    listofsequences=''.join(sequences)
        	print(listofsequences)
    map = {'A' : 1, 'R' : 2, 'D' : 3, 'N' : 4, 'C': 5, 'E': 6, 'Q': 7, 'G': 8, 'H': 9, 'I': 10, 'L': 11, 'K': 12, 'M': 13, 'F': 14, 'P': 15, 'S': 16, 'T': 17, 'W': 18, 'Y': 19, 'V': 20}
    seqinnumbers=[]
    for seq in listofsequences:
        newseq = []
        for aa in seq:
            number = map[aa]
            newseq.append(number)
        seqinnumbers.append(newseq)
    for windowlen in range(3,23,2):
        n = windowlen // 2
        listofwindows = []
        listofstates = []
        for count in range(len(seqinnumbers)):   
            for aa in range(len(seqinnumbers[count])):
                if aa in range(0, n):
                    listof0 = [0] * (n - aa)
                    listofwindows.append(np.array(listof0 + seqinnumbers[count][0:aa + n + 1]))
                    listofstates.append(P[count][aa])
                elif aa in range(len(seqinnumbers[count]) - n,len(seqinnumbers[count])):
                    listof0 = [0] * (n + 1 + aa -len(seqinnumbers[count]))
                    listofwindows.append(np.array(seqinnumbers[count][aa - n:len(seqinnumbers[count])] + listof0))
                    listofstates.append(P[count][aa])
                else:
                    listofwindows.append(np.array(seqinnumbers[count][aa - n :aa + n + 1]))
                    listofstates.append(P[count][aa])
    listalls = np.array(listofstates)

if __name__=="__main__":
    (parser('test'))
