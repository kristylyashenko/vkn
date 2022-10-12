from array import *

arr = array('i', [1, 2, 3, 4, 5, 6, 7])

for element in arr:
    divisors = []
    i = 1
    while i <= element: 
        if element % i == 0:
            divisors.append(str(i))
        i +=1
    
    divisors = ", ".join(divisors)

    print(f'element: {element} та його додатні дільники: {divisors}')

