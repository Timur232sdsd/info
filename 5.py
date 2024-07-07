##d = set()
##for i in range(1, 1000):
##    s = bin(i)[2:]
##    m = int(sum(map(int, str(s))))%2
##    s = s + str(m)
##    m = int(sum(map(int, str(s))))%2
##    s = s + str(m)
##    n = int(s, 2)
##    if n < 80:
##        d.add(n)
##print(len(d))

for m in range(1, 1000000):
    n = 120
    s = str(n)
    q = str(m)
    k = 1
    c = 1
    for i in range(len(s)):
        if s[i]!='0' and int(s[i])%2==0:
            k*=int(s[i])
    for i in range(len(q)):
        if q[i]!='0' and int(q[i])%2==0:
            k*=int(q[i])
    for i in range(len(s)):
        if s[i]!='0' and int(s[i])%2!=0:
            c*=int(s[i])
    for i in range(len(q)):
        if q[i]!='0' and int(q[i])%2!=0:
            c*=int(q[i])
    if abs(k - c) == 29:
        print(m)
        break
    
            
