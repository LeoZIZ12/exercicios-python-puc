n=int(input("digite um numero inteiro: "))
x=1
soma=0
while x <= n:
    if n % x==0:
        soma+=x
    x=x+1
print(soma)