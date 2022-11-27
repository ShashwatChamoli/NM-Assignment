import numpy as np
import matplotlib.pyplot as plt

#Reading data points
x,y=np.loadtxt("data.dat",unpack=True)

#Lagrange interpolation:
def lag_int_pol(xpoint,x,prod,i):
    for j in range(len(x)):
        if i!=j:
            prod*=(xpoint-x[j])/(x[i]-x[j])
            
    return prod

def lag_int(xpoint,x,y):
    sum=0
    for i in range(len(x)):
        sum+=lag_int_pol(xpoint,x,y[i],i)
    return sum

#Lagrange 1st derivative
def lag_derivative_pol(xpoint,x,prod,i):
    sum=0
    for j in range(len(x)):
        if i!=j:
            sum+=1/(xpoint-x[j])
            
    return sum*lag_int_pol(xpoint,x,prod,i)
    
def lag_derivative(xpoint,x,y):
    sum=0
    for i in range(len(x)):
        sum+=lag_derivative_pol(xpoint,x,y[i],i)
    return sum
print('The interpolated value at 2.5 is ',lag_int(2.5,x,y))

#Newton Raphson
def root(lag_int,lag_derivative,s,x,y,e):
    a=0
    while(True):
        a=lag_int(s,x,y)
        s=s-a/lag_derivative(s,x,y)
        if(abs(a)<abs(e)):
            break
    return s
print('First root is ',root(lag_int,lag_derivative,3.1,x,y,0.0000001))
print('Second root is ',root(lag_int,lag_derivative,0.5,x,y,0.0000001))

#Simpson's rule
def simp(f,a,b):
    n=100
    delx=(b-a)/n
    A=(delx/3)*(f(a,x,y)+f(b,x,y))
    A1=0
    for i in range(1,n,2):
        A1=A1+(delx/3)*4*(f(a+(i)*delx,x,y))
    for i in range(2,n-1,2):
        A1=A1+(delx/3)*2*(f(a+i*(delx),x,y))
    Area=A+A1
    return Area
print('Value after simpsons integration is ',simp(lag_int,0,4))

#Checking where the integral is zero
def root2(simp,lag_int,s,x,y,e):
    a=0
    while(True):
        a=simp(lag_int,0,s)/lag_int(s,x,y)
        s=s-a
        if(abs(a)<abs(e)):
            break
    return s
print('The value of x till where the integration from 0 is zero:',root2(simp,lag_int,1.1,x,y,0.0000001))

#Finding coefficients
def lag_derivative2(xpoint,x,y):
    h=0.001
    c=(-lag_derivative(xpoint+2*h,x,y)+8*lag_derivative(xpoint+h,x,y)-8*lag_derivative(xpoint-h,x,y)+lag_derivative(xpoint-2*h,x,y))/(12*h)
    return c

def lag_derivative3(xpoint,x,y):
    h=0.001
    c=(-lag_derivative(xpoint+2*h,x,y)+16*lag_derivative(xpoint+h,x,y)-30*lag_derivative(xpoint,x,y)+16*lag_derivative(xpoint-h,x,y)-lag_derivative(xpoint-2*h,x,y))/(12*h*h)
    return c
#Function and derivative of the equation containing w
def for_w(w):
    return 3*lag_derivative2(0,x,y)*w-3*lag_derivative(0,x,y)*(w**2)+lag_int(0,x,y)*(w**3)-lag_derivative3(0,x,y)
def for_w_der(w):
    return 3*lag_derivative2(0,x,y)-6*lag_derivative(0,x,y)*w+3*lag_int(0,x,y)*(w**2)

#To find the root of equation containing w
def root3(f,g,a):
    h = f(a)/g(a)
    while abs(h) >= 0.0001:
        h=f(a)/g(a)
        a=a-h
    return a

#Printing the coefficients
c=lag_int(0,x,y)
w=root3(for_w,for_w_der,2)
b=lag_derivative(0,x,y)-(c*w)
a=(lag_derivative2(0,x,y)+c*(w**2)-2*lag_derivative(0,x,y)*w)/2
print('The value of a is',a)
print('The value of b is',b)
print('The value of c is',c)
print('The value of w is',w)

def h(x,a,b,c,w):
    return (a*(x**2)+(b*x)+c)*(np.exp(w*x))
plt.plot(x,h(x,a,b,c,w),"r")
plt.scatter(x,lag_int(x,x,y))
plt.show()