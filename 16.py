from functools import *

@lru_cache(None)

def f(n):
    if n < 3: return n+1
    if n >= 3 and n%2==0: return f(n-2)+n-2
    if n >= 3 and n%2!=0: return f(n+2)+n+2
k = 0
for n in range(1, 10_000):
    try:
        if f(n) >= 10_000 and f(n) < 100_000:
            k+=1
    except:
        pass
print(k)
