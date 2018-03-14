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
            dictionary[ids]['seq']= sequences
            #print(sequences)
        else:
            topologies=line.rstrip()
            dictionary[ids]['topology'] = topologies
            #print(topologies)
    print(dictionary)                     
if __name__=="__main__":
    (dataset('test'))
    

