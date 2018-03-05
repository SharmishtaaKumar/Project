def parser(file_name):
    filehandle = open(file_name,'r')
    text = filehandle.readlines()
    topologies=[]
    
    
    A=[]
    for line in text:
        if line[0]!= '>': 
            if line[0]!= 'M':
            	topologies.append(line.rstrip())
            	#print (topologies)
            	topology=[]
            	for tops in topologies:
            	    topology=list(tops)
            	print(topology)
    dicttop = {'I':'1', 'M':'2', 'O':'3'}
    print(dicttop.items())
    for letter in topology:
        #print(letter)
        newtop=[]
        for z in letter:
            #print(z)
            for key,value in list(dicttop.items()):
                print (value)
                if z==key:
                    newtop.extend(value)
                    print(newtop)
            
            
    			
    
            		
            		
if __name__=="__main__":
     (parser('test'))
     



