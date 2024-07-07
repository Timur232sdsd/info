##def f(a, b, m):
##    if a*b>=63: return m%2==0
##    if m==0: return 0
##    h = [f(a+1,b,m-1), f(a,b+1,m-1),f(a*2,b,m-1),f(a,b*2,m-1)]
##    return any(h) if m%2!=0 else all(h)
##n = 2
##print([s for s in range(1,32) if f(n, s, 2) and not(f(n, s, 1))])
##print()
##print([s for s in range(1,32) if not(f(n, s, 1)) and f(n, s, 3)])
##print()
##print([s for s in range(1,32) if not(f(n, s, 2)) and not(f(n, s, 0)) and f(n, s, 4)])
def f(a, m):
    if a<=0: return m%2==0
    if m==0: return 0
    h =[f(a-1, m-1),f(a-2, m-1)]
    if a>=4: h += [f(a-4, m-1)]
    return any(h) if m%2!=0 else all(h)
##print([s for s in range(10, 99) if f(s, 2) and not(f(s, 1)) and not(f(s, 0))])
##print()
print([s for s in range(1, 43) if f(s, 5) and not(f(s, 1)) and not(f(s, 3))])
##print()
##print([s for s in range(1, 43) if f(s, 4) and not(f(s, 2)) and not(f(s, 0))])
