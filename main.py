from itertools import *
from ipaddress import *
from functools import *
##def f(x,y,z, w):
##    return (y<=(not(x<=z))) or w
##
##for a1,a2,a3,a4,a5,a6,a7 in product([0,1], repeat=7):
##    t = [(a1,0,a2,a3),(0,1,a4,a5),(1,a6,a7,0)]
##    if len(t)==len(set(t)):
##        for p in permutations('xyzw'):
##            if [f(**dict(zip(p,r))) for r in t] == [0,0,0]:
##                print(p)


##for n in range(1, 13):
##    s = bin(n)[2:]
##    if n%2==0: s = '10' + s
##    else: s = '1' + s + '01'
##    r = int(s, 2)
##    print(r)
##s = sorted('ФОКУС')
##k = 0
##
##for x in product(s, repeat=5):
##    c = ''.join(x)
##    k+=1
##    if c.count('Ф')==0 and c.count('У')==2:
##        m = k
##        z = c
##print(m, z)
##s = '8'*83
##while '111' in s or '88888' in s:
##    if '111' in s: s = s.replace('111','88',1)
##    else: s = s.replace('88888','8',1)
##print(s)
##net = ip_network('112.160.0.0/255.240.0.0')
##c = 0
##for ip in net:
##    b = bin(int(ip))[2:].zfill(32)
##    if b.count('1')%3!= 0:
##        c+=1
##print(c)
##def f(x):
##    a = []
##    while x:
##        a = [x%7] + a
##        x//=7
##    return a
##
##for n in range(1, 2031):
##    x = 7**91+7**160-n
##    if f(x).count(0)==70:
##        print(n)

##def f(x):
##    return x%a==0 or ((70 <= x <= 90) <= x%22!=0)
##
##for a in range(1, 10000):
##    if all(f(x)==1 for x in range(70,91)):
##        print(a)
##f = open('17.txt')
##a = [int(x) for x in f]
##b = len([int(x) for x in a if x%32==0])
##c = []
##for i in range(len(a)-1):
##    if (a[i] < 0 or a[i+1] < 0) and (a[i]+a[i+1]) < b:
##        c.append(a[i]+a[i+1])
##print(len(c), max(c))

##def f(s, m):
##    if s>57: return m%2==0
##    if m==0: return 0
##    h = [f(s+1,m-1), f(s+4, m-1), f(2*s, m-1)]
##    return any(h) if m%2!=0 else all(h)
##print([s for s in range(1,58) if not(f(s, 2)) and f(s, 4)])
##def f(x, y):
##    if x > y: return 0
##    if x == y: return 1
##    else: return f(x+1, y) + f(x+2, y) + f(x+3, y)
##print(f(5,7)*f(7,11))
##s = open('24.txt').readline()
##m = l = k = 0
##q = '-*'
##w = '0789'
##for i in range(len(s)):
##    if s[i] in q and s[i+1] in w:
##        k += 1
##        if k > l: l = k
##    else: k = 0
##print(l)

##def f(x):
##    d = set()
##    for i in range(2,int(x**0.5+1)):
##        if x%i==0: d|={i, x//i}
##    return sorted(d)
##
##for x in range(700_000, 701_000):
##    if len(f(x)) > 1:
##        m = max(f(x))+min(f(x))
##        if m%10==4:
##            print(x, m)

##f = open('27A.txt')
##n = int(f.readline())
##a = [int(x) for x in f]
##ml, mn = 0, 10**20
##for i in range(n):
##    s = 0
##    for j in range(i, n):
##        s+=a[j]
##        if s%2!=0 and s < mn or (s ==mn and ml < j-i+1):
##                ml = j-i+1
##                mn = s
##print(ml)
##
##f = open('27B.txt')
##n = int(f.readline())
##s = 0
##m = [-10**20]*2
##l = [-10**20]*2
##mn = 10**20
##ml = 0
##for i in range(n):
##    x = int(f.readline())
##    s+=x
##    if s%2!=0:
##        if s < mn or (s==mn and ml < i+1):
##            mn = s
##            ml = i+1
##    s1 = s - m[(s%2+1)%2]
##    l1 = i+1 - l[(s%2+1)%2] 
##    if s1 < mn or (s==mn and ml < l1):
##        mn = s1
##        ml = l1
##    if m[s%2] < s:
##        m[s%2] = s
##        l[s%2] = i+1
##print(ml)
f = open('9.txt')
k = 0
for s in f:
    a = [int(x) for x in s.split()]
    a1 = [x for x in a if a.count(x)==1]
    a3 = [x for x in a if a.count(x)==3]
    if len(a1)==3 and len(a3)==3 and sum(a3)**2>sum(a1)**2:
        k+=1 
print(k)













    







