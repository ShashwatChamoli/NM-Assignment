import random
import numpy as np
def rand(n):
    a=[]
    for i in range(0,n):
        a.append(random.randint(1,1000))
    return a
a=rand(20)
print('20 random numbers are ')
print(a)    
print('20 random numbers in ascending order are ')
for i in range(0, 20):    
    for j in range(i+1, 20):    
        if(a[i] > a[j]):    
            b = a[i];    
            a[i] = a[j];    
            a[j] = b;
print(a)        
