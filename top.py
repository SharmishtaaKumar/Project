def parser(file_name):
    filehandle = open(file_name,'r')
    text = filehandle.readlines()
    topologies=[]
    for line in text:
        if line[0]!= '>': 
            if line[0]!= 'M':
            	topologies.append(line.rstrip())
    #print (topologies)    	
    dicttop = {'I': 1, 'M': 2, 'O': 3}
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
    print(len(y))	
if __name__=="__main__":
    parser('test')
