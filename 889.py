def f(x, y, z):
    if x == 20  or z == 2 or x > 41:
        return 0
    if x == y:
        return 1
    else:
        return f(x-1, y, z+1) or f(x+2, y, z) or f(x*2, y, z)
print(f(3, 30, 0)*f(30, 40, 0))
