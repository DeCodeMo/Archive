import math as ma
import numpy as np

'''Determine damping given characteristic (2nd ord) polynomial and return roots'''

def chareq_order2(poly):
    # for testing: 
    # Undamped case          --> y' + y + 3  = 0 --> charpoly = r^2 + r + 3  = 0 --> poly array = [1,1,3]
    # Overdamped case        --> y' + 4y + 3 = 0 --> charpoly = r^2 + 4r + 3 = 0 --> poly array = [1,4,3]
    # Critically Damped case --> y' + 4y + 4 = 0 --> charpoly = r^2 + 4r + 4 = 0 --> poly array = [1,4,4]
    a = poly[0]
    b = poly[1];
    c = poly[2];
    b2 = b**2
    ac4 = 4*a*c
    det = b2-ac4
    if b2 > ac4:
        damping = 'Overdamped'
        roots = 'Real and Distinct'
    if b2 < ac4:
        damping = 'Underdamped'
        roots = 'Complex'
    if b2 == ac4:
        damping = 'Critically damped'
        roots = 'Real and Repeated'
    if b2 == 0:
        damping = 'Undamped'
        roots = '-->'
    if det < 0:
        det = det*-1
        imag = (ma.sqrt(det))/(2*a)
        re = (-b)/(2*a)
        print(f"Roots = {roots}, Damping = {damping}, (r1,r2) = ({re} + {imag:0.2f}i , {re} - {imag:0.2f}i)")
    else:
        r1 = ((-b)/(2*a)) + (ma.sqrt(det)/(2*a))
        r2 = ((-b)/(2*a)) - (ma.sqrt(det)/(2*a))
        print(f"Roots = {roots}, Damping = {damping}, (r1,r2) = ({r1} , {r2})")

def test_main():
    # poly is ax^2 + bx + c
    # for a, b, c = 1, 8, 32
    # assert --> -4 (+-) 4i "complex roots", underdamped system
    pass

def main():

    chareq_order2([1,8,32])



if __name__=="__main__":
    main()