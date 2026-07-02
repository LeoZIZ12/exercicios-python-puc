def contar_ate_zero(n):
    if n==0:
        return
    else:
        print(n)
        contar_ate_zero(n-1)

n=10

contar_ate_zero(n)