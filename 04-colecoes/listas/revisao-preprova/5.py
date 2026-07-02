numeros=[10,29,40,10,20]
diferenca=0
lista_diferencas=[]
for i in range(len(numeros)):
    diferenca=numeros[i]-numeros[i-1]
    lista_diferencas.append(diferenca)
maior=lista_diferencas[0]
for i in range(len(lista_diferencas)):
    if lista_diferencas[i]>maior:
        maior=lista_diferencas[i]
print(maior)