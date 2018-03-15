test = "../datasets/test"
def dataset(filename):
    filehandle = open(filename,'r')
    text = filehandle.readlines()
    dictionary={}
    sequences=[]
    topologies=[]
    for line in text:
        if line[0]=='>':
            ids=line.rstrip()
            dictionary[ids]= {}
        elif line[0]=='M':
            sequences=line.rstrip()
            dictionary[ids][0]= sequences
            #print(sequences)
        else:
            topologies=line.rstrip()
            dictionary[ids][1] = topologies
            #print(topologies)
    return dictionary               
if __name__=="__main__":
    (dataset(test))
    

