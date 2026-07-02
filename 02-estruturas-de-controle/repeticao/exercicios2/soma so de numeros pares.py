n=float(input("digite um numero:"))
soma=0
while n!=0:
    if n%2==0:
        soma=soma+n
        n=float(input("digite mais um numero"))
    else:
        n=float(input("digite mais um numero"))
if n==0:
    print(soma)