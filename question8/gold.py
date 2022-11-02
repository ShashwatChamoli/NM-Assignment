import numpy as np
import matplotlib.pyplot as p
import sys
sys.path.insert(0,'/Users/shashwatchamoli/Desktop/assignment1/question5')
import fibo as f
def gold(n):
  a=f.fibo(n)
  b=f.fibo(n+1)
  c=b/a
  return c
print('The approximate value of golden ratio is',gold(1000))
e=[]
for i in range (2,20):
 y=gold(i)
 e.append(y)
x=np.linspace(2,19,18)
p.plot(x,e,"r")
p.title("Golden ratio v|s n")
p.xlabel("n")
p.ylabel("Golden ratio")
p.show()
