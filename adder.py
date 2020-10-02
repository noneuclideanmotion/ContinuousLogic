import cmath
import random as r

def _not(a):
    return 1-a

def _and(a, b):
    return a*b

def _or(a, b):
    return a+b-_and(a, b)

def _xor(a, b):
    return _or(a, b)-_and(a, b)

def _add(a, b):
    carry = 0
    s = []
    for i in range(len(a)-1, -1, -1):
        a[i] = float(a[i])
        b[i] = float(b[i])
        s.insert(0, _xor(_xor(a[i], b[i]), carry))
        carry = _or(_and(_xor(a[i], b[i]), carry), _and(a[i], b[i]))
    if carry != 0:
        s.insert(0, carry)
    return s

while True:
    a = []
    b = [0]
    while len(a) != len(b):
        a = input("enter input A: ").split(" ")
        b = input("enter input B: ").split(" ")
    print(_add(a, b))
    print("Decimal A " + str(sum((2**x)*a[len(a)-x-1] for x in range(len(a)))))
    print("Decimal B " + str(sum((2**x)*b[len(b)-x-1] for x in range(len(b)))))
    print("Decimal sum " + str(sum((2**x)*_add(a,b)[len(_add(a, b))-x-1] for x in range(len(_add(a, b))))))
        


