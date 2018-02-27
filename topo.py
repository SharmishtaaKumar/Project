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
            	tops=list(topologies[0])
            	#print(tops)
            	dicttop = {'I':1, 'M':2, 'O':3}
            	#print(list(dicttop.keys()))
    for letter in tops:
    	for i in list(dicttop.keys()):
    		if letter==i:
    			A.append(dicttop.get(i))
    print (A)
            		
            		
if __name__=="__main__":
     (parser('test1'))
     



