import random  

f=open('numbers.txt',"r",encoding="utf-8")   
l=open('full_numbers.txt',"w",encoding="utf-8")   
z=f.readlines() 
for key in z: 
    first =str(random.randint(1000,9999))
    first = first + key
    l.write (first+"\n")
l.close()  
f.close()
