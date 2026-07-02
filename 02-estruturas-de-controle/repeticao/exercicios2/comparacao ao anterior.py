valor=float(input("digite um numero: "))
igual_anterior=0
maior_anterior=0
menor_anterior=0

while valor!=0:
    anterior=valor
    valor=float(input("digite um numero: "))
    if valor!=0:
        if valor==anterior:
            igual_anterior=igual_anterior+1
        elif valor>anterior:
            maior_anterior=maior_anterior+1
        elif valor<anterior:
            menor_anterior=menor_anterior+1
if valor==0:
    print("igual ao anterior= ", igual_anterior)
    print("maior que o anterior= ", maior_anterior)
    print("menor que o anterior= ", menor_anterior)