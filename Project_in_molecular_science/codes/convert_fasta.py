tempfile="../datasets/50unknownproteins"
fasta_data="../fasta_data/"
def fasta(filename):
    filehandle = open(filename,'r')
    text = filehandle.readlines()
    dictionary={}
    topologies=[]
    sequences=[]
    identity=[]
    for line in text:
        if line[0]=='>':
            ids=line.rstrip()
            
        elif line[0]=='M':
            sequences=line.rstrip()
            dictionary[ids]=sequences
   
    for new_id in dictionary:
        newfile=str(new_id)+ '.fasta'
        sequence=dictionary[new_id]
        fasta_files=open(fasta_data+newfile, "w")
        fasta_files.write(new_id+ '\n' + sequence)
    fasta_files.close()
    return dictionary, topologies
   
if __name__=="__main__":
    fasta(tempfile)
