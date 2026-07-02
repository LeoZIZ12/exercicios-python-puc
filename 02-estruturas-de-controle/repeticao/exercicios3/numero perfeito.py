n=int(input("digite um numero inteiro: "))
x=1
soma=0
while x < n:
    if n % x==0:
        soma+=x
    x=x+1
if soma==n:
    print(f"{n} é um numero perfeito")
else:
    print(f"{n} nao é um numero perfeito")