from itertools import *
def f(x, y, z):
    return not(x) or (y and not(z))

t = [(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1),(1,1,0),(1,1,1)]
for p in permutations('xyz'):
    if [f(**dict(zip(p, r))) for r in t] == [1,1,0,1,1,1,0,0]:
        print(p)
        
