import csv
T={}
with open('some.csv', "w" ) as f:    
    writer = csv.writer(f,delimiter=";") 
    with open("WORD.txt") as x:
        for line in x.readlines():
            if line not in T:
                T [line.replace("\n", '')]=0
            T[line.replace("\n",'')]+=1
    for i in T.keys():
        writer.writerow([i,T[i]])
