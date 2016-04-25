import os  
filename = raw_input('please enter a file name:')  
n=0  
f=open(filename,'r') 
alllines = f.readlines()
for i in alllines:  
    print i.strip()
    n+=1  
    if n==25:  
        n=0  
        os.system('pause')  
f.close()