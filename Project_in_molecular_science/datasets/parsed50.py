
def dataset(filename):
    filehandle = open(filename,'r')
    text = filehandle.readlines()
    with open("50proteinstobepredicted",'w') as pr:
        for h in range(len(text)):
            if text[h].startswith('>'):
                pr.write(text[h])
                pr.write(text[h+1])
                pr.write("\n")
		        
if __name__=="__main__":
    (dataset('the50'))
