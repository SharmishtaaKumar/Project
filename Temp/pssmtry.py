def fasta(file):
    filehandle = open(file,'r')
    text = filehandle.readlines()
    fasta=[]
    for line in text:
        if line[0]=='>' or line[0]=='M':
            fasta.append(line.rstrip())
            
    print(fasta)
    
if __name__=="__main__":
    fasta('test1')
            
