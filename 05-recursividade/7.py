def soma_ate(n):
    if n==0:
        return 0
    else:
        return n + soma_ate(n-1)
    
n=int(input())
print(soma_ate(n))