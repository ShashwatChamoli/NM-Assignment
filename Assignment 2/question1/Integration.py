import numpy as np
def trap(f,a,b):
    n=1000
    delx=(b-a)/n
    A=delx*(f(a)+f(b))/2
    A1=0
    for i in range (1,n):
        A1=A1+f(a+delx*i)
    Area=A+delx*A1
    return Area
    
def simp(f,a,b):
    n=1000
    delx=(b-a)/n
    A=(delx/3)*(f(a)+f(b))
    A1=0
    for i in range(1,n,2):
        A1=A1+(delx/3)*4*(f(a+(i)*delx))
    for i in range(2,n-1,2):
        A1=A1+(delx/3)*2*(f(a+i*(delx)))
    Area=A+A1
    return Area
def f(x):
    return x*np.log(x)-x

print('Trap: ')
print(trap(f,1,3))
print('Simp: ')
print(simp(f,1,3))
