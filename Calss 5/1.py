def print_root(a,b,c):
    r1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    r2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    return r1

def plus(x,y):
    p = x + y
    return p

banana = 10.0
print(plus(banana, print_root(1,2,-8)))