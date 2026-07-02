n=float(input("digite um numero:"))
soma=0
qtd_n=0
while n!=0:
    soma=soma+n
    qtd_n=qtd_n+1
    n=float(input("digite mais um numero:"))
if n==0:
    media=soma/qtd_n
    print("media=",media)