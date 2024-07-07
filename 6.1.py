k=0
for x in range(-100, 100):
    for y in range(-100, 100):
        if x < 0 and y < 1/(3**0.5) * x + 30 and y > -1/3**0.5 * x:
            k+=1
print(k)
