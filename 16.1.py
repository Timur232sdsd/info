##from functools import *
##
##@lru_cache(None)
##
##def f(x, y):
##    if x>y: return 0
##    if x==y: return 1
##    else:
##        return f(x+1, y) + f(int(bin(x)[2:]+'0', 2), y) + f(int(bin(x)[2:]+'1', 2), y)
##print(f(int('100', 2), int('11101', 2))))



def f(x, y, k):
    if x>y or k>6: return 0
    if x%2==0: k+=1
    if x==y and k==6: return 1
    else: return f(x+1,y,k) + f(x+3,y,k) + f(x+5,y,k)

print(f(3, 25, 0))
