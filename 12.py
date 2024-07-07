##s = '>' + 11*'1'+12*'2'+30*'3'
##
##while '>1' in s or '>2' in s or '>3' in s:
##    if '>1' in s:
##        s = s.replace('>1', '22>', 1)
##    if '>2' in s:
##        s = s.replace('>2', '2>', 1)
##    if '>3' in s:
##        s = s.replace('>3', '1>', 1)
##print(s)
##print(s.count('2')*2 + (s.count('1')))
##print(sum([int(d) for d in s[:-1]]))
##
##d = set()
##for i in range(1, 1_000):
##    s = i*'5'
##    while '555' in s or '888' in s:
##        s = s.replace('555', '8', 1)
##        s = s.replace('888', '55', 1)
##    d.add(s)
##print(len(d))
a = 'ИНФОРМАТИКА'
m = 9
b = a[m]
for i in range(4, 6):
    c = a[i-1]
    b += c

for i in range(1, 4):
    c = a[i-1]
    b+= c
print(b)
