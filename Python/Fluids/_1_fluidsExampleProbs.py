import sympy as sm
from sympy import symbols as sym
from sympy import *
import numpy as np


def tau(mu, u, h):
    y = sym('y')  
    du = diff(u,y)
    du_y = du.subs(y,h)
    tau = mu*du_y
    return tau

def fluidHeight_stdUnits(Pg,Pw,g,dh):
    Pl = Pw*g
    P = Pg*144
    Pls = P/Pl
    h = Pls-dh
    print(f"Fluid Height (h) = {h:0.3f} ft") 
    return h



y = sym('y')

# Given
mu = 0.332
u = (8*y-0.3*y**2)
hp = 4  # plate
hs = 0 # fixed surface

# solve
# @y = 4mm (top plate)
Tp = tau(mu,u,hp)
Ts = tau(mu,u,hs)
print(f"Shear Stress @ plate = {Tp:0.2f} Pa\nShear Stress @ fixed surface = {Ts:0.2f} Pa")

    
dh = 0.5
Pg = 24 #psi
Pw = 1.94 #slug/ft^3
Phg = 26.3 #slug/ft^3
g = 32.2

fluidHeight_stdUnits(Pg,Pw,g,dh)
fluidHeight_stdUnits(Pg,Phg,g,dh)

WaterHeight = fluidHeight_stdUnits(Pg,Pw,g,dh)
mercuryHeight = fluidHeight_stdUnits(Pg,Phg,g,dh)

def compare(a, b):
    if a > b:
        print(f"{a:0.3f} is greater than {b:0.3f}")
    else:
        print(f"{b:0.3f} is greater than {a:0.3f}")