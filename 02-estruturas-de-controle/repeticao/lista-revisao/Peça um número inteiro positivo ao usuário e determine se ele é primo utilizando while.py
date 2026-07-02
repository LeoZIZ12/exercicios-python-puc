n=int(input("digite um numero inteiro positivo: "))
q=n
contador=0
while n > 0:
    if q%n==0:
        contador+=1
    n=n-1
if contador==2:
    print("O numero é primo")