S=input("введіть символи:") 
spisok=list(s) 
x=set(spisok) 
print(x) 
a=set() 
n=set() 
c=set() 
for i in x: 
    if i.isdigit()==True: 
        n.add(i) 
    elif i.isalpha()==True:
        a.add(i) 
    else: 
        c.add(i) 
print(n) 
print(a) 
print(c)
