numeros=[1,2,3]
valor_repetido=False
for i in range(len(numeros)):
    if numeros[i]==numeros[i-1]:
        valor_repetido=True
print(valor_repetido)