numero=input("digite um numero binario: ")
decimal=0
expoente=0
i=len(numero)-1
while i >=0:
    digito=int(numero[i])
    decimal=decimal+digito*(2**expoente)
    expoente=expoente+1
    i-=1
print(decimal)