numeros=[1,2,3,4,4,4,]
crescente=True
for i in range(len(numeros)):
    if numeros[i-1]>numeros[i]:
        crescente=False
print(crescente)
    