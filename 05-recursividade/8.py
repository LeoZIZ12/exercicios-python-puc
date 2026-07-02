def pot(n, e):
    if e == 0:
        return 1
    if n == 1:
        return n
    else:
        return n * pot(n, e-1)

n=int(input())
e=int(input())
print(pot(n, e))