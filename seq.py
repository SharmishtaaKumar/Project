
import numpy as np
def parser(file_name):
    filehandle = open(file_name,'r')
    text = filehandle.readlines()
    sequences=[]
    d={}
    A='0'
    newlist=[]
    listnew=[]
    for line in text:
        if line[0]=='M':
        	sequences.append(line.rstrip())
        	#print (sequences)
        	seq = list(sequences[0])
        	seqs=[A]+seq+[A]
        	#print(seqs)
        	a_a=['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
        	#print (a_a)
        	binary= np.zeros(shape=(20,20), dtype=int)
        	np.fill_diagonal(binary, 1)
        	#print (binary)
        	newbinary=binary.tolist()
        	d= zip(a_a,newbinary)
        	dictseq = dict(d)
        	c={'0': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
        	dictseq.update(c)
        	#print (c)
        	#print (dictseq)
    i=iter(seqs)
    numofwin = int(len(seqs)-3/1)+1
    for i in range(0,numofwin):
    		newseq=(seqs[i:i+3])
    		arr= ''.join(newseq)
    		#print (newseq)
    		for j in arr:
    			newlist.extend(dictseq.get(j))
    			#print(newlist)
    		listnew=newlist
    		#print(listnew)
    		newarray=np.array(listnew)
    		print(newarray)
    		newlist.clear()
if __name__=="__main__":
    (parser('test1'))
