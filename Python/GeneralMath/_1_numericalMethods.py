import numpy as np
#from matplotlib import pyplot as plt

##---------------------- ODE ------------------------##

def f(x,y):
    """---Define your ODE here---
       Params:(x,y)
       **Redefine as needed***
    """
    return 6*y - y**2 # function
   
##-------------------- Main -------------------------##
'''Just uncomment, define parameters, and run this script
   Params: (inital-x, final-x, initial-y, number of steps)
'''
def main():
    
    euler(0,0.1,9,1)



##------------------------- Methods -------------------------##
'''Numerical methods are defined here'''


def euler(x0,xf,y0,n):
    """---Standard Euler method---
       Params:(inital-x, final-x, initial-y, number of steps)
    """
    h = 0.1 #(xf-x0)/n
    x = x0
    y = y0
    n = range(n)
    for i in n:
        dydx = f(x,y) # 1st order ODE being evaluated 
        y = y + h * dydx # next iteration
        x = x + h # next step
        print(f"step = {h:0.3f}, x = {x:0.2f}, y = {y:0.4f}")
        
def euler2(x0,xf,y0,n):
    """---Improved Euler method---
        params: (inital-x, final-x, initial-y, number of steps)
    """
    h = (xf-x0)/n
    x = x0
    y = y0
    n = range(n)
    for i in n:
        k1 = f(x,y) # first series
        y = y + h * k1
        x = x + h
        k2 = f(x,y) # second series
        k = (k1 + k1)/2 # mean of both series
        y = y + h * k
        print(f"step = {h:0.3f}, x = {x:0.2f}, y = {y:0.4f}")



def rK_4(x0,xf,y0,n):
    """---Runge Kutta method---
       params: (inital-x, final-x, initial-y, number of steps)
    """
    
    h = (xf-x0)/n
    x = x0
    y = y0
    n = range(n)
    a = 0.5
    for i in n:   
        k1 = f(x,y)
        x = x+a*(h)
        y = y+a*(h*k1)  
        k2 = f(x,y)
        y = y+a*(h*k2)
        k3 = f(x,y)
        x = x+a*(h)
        y = y+a*(h*k3)
        k4 = f(x,y)
        
        rK = (1/6)*(k1+2*k2+2*k3+k4)
        y = y + h*rK
        print(f"step = {h:0.3f}, x = {x:0.2f}, y = {y:0.4f}")


if __name__ == "__main__":
    main()