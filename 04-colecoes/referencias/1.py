lista=[1,-1,2,4,5,-3]
lista_zerada=lista.copy()

def zerar_negativos(x):
    for i in range(len(x)):
        if x[i]<0:
            x[i]=0
    return x

zerar_negativos(lista_zerada)

print(lista_zerada)
print(lista)