import math as ma
import numpy as np
from sympy import *

#helpers
sqrt = ma.sqrt
syms = symbols
# Define variables
M,L,T,F = syms('M L T F') # mass, length, time, force

MLT = {
    'A':L**2,
    'V':L**3,
    'v':L/T,
    'a':L/(T**2),
    'w':1/T,
    'F':(M*L)/(T**2),
    'm':M,
    'p':M/(L**3),
    'gamma':M/((L**2)*(T**2)),
    'P':M/(L**3),
    'mu':M/(L*T),
    'nu':(L**2)/T,
    'Wdot':(M*(L**2))/(T**3),
    'Q':(L*3)/T,
    'mdot':M/T,
    'sigma':M/(T**2),
    'W':(M*L)/(T**2),
    'Tau':(M*L**2)/(T**2),
    'L':L
}

FLT = {
    'A':L**2,
    'V':L**3,
    'v':L/T,
    'a':L/(T**2),
    'w':1/T,
    'F':F,
    'm':(F*T**2)/L,
    'p':(F*T**2)/(L**4),
    'gamma':F*(L**3),
    'P':F*(L**2),
    'mu':(F*T)/(L**2),
    'nu':(L**2)/T,
    'Wdot':(F*L)/T,
    'Q':(L*3)/T,
    'mdot':(F*T)/L,
    'sigma':F/L,
    'W':F,
    'Tau':F*L,
    'L':L
}

def example_dimAnalysis():
    Q = FLT['Q']
    p = FLT['p']
    L = FLT['L']

    (Q*p)/L
    print((L**3)*(L**(-1)))

    pw = ((1000)*6*0.05)/(1e-3)
    print(pw)
    po = (880*8)/(30.2e-3)
    print(po)
    print(po/pw)

    pm = 1.202
    um = 18.1e-6
    Lm = 1.5
    pp = 0.4135
    up = 14.58e-6
    Lp = 15
    vp = 1140
    Rep = (pp*vp*Lp)/(up)
    print(Rep)

    vm_Rem = (pm*Lm)/um
    vm = Rep/vm_Rem
    print(vm)
    
example_dimAnalysis()
