def parser(file_name):
    filehandle = open(file_name,'r')
    text = filehandle.readlines()
    topologies=[]
    d={}
    for line in text:
        if line[0]!= '>': 
            if line[0]!= 'M':
            	topologies.append(line.rstrip())
            	#print (topologies)
            	topology=[]
            	for tops in topologies:
            	    topology=list(tops)
            	print(topology)
    d={'I':1,'O':2,'M':3}
    print(d.items())
if __name__=="__main__":
    parser('test')
