numero=float(input("digite um numero: "))
soma=0
while numero!=0:
    soma=soma+numero
    numero=float(input("digite mais um numero"))
    if numero==0:
        print(soma)