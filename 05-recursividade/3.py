def some_ate(n):
    soma=0
    if n==0:
        return 0
    else:
        return n + some_ate(n-1)
    
n=3

print(some_ate(n))