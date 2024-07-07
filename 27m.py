f = open('27-A.txt')
n = int(f.readline())
a = [int(x) for x in f]

pref = [0]*n

for i in range(n): pref[i] = pref[i-1] + a[i]
pref = [0]+pref


mx_b = [-10**20]*(n+1)
for i in range(n):
    mx_b[i] = max(mx_b[i-1], pref[i])

mx_a = [-10**20]*(n+1)
mx_a[-1] = pref[-1]
for i in range(n-1, -1, -1):
    mx_a[i] = max(mx_a[i+1], pref[i])
mxb = -10**20

for j in range(2, n-2):
    mxb = max(mxb, mx_a[j+2] - 2*pref[j] + mx_b[j-2])
print(mxb)












f = open('27-A.txt')
n = int(f.readline())
a = [int(x) for x in f]

pref = [0]*n

for i in range(n): pref[i] = pref[i-1] + a[i]

pref = [0] + pref

b = [10**20]*(n+1)
for i in range(n): b[i] = min(b[i-1], pref[i])
a = [10**20]*(n+1)

a[-1] = pref[-1]
for i in range(n-1, -1, -1): a[i] = min(a[i+1], pref[i])
mx = 10**20


for j in range(2, n-2):
    mx = min(mx, a[j+2] + b[j-2] - 2*pref[j])
print(mx)
















