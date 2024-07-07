def f(x, y):
    if x == y: return 1
    if x > y: return 0
    if x < y: return(f(x+1, y) + f(x*10+1, y) + f(5*x, y))
print(f(1, 410))
                    
