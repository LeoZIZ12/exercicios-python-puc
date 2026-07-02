def existe(lista, valor, i):
    if i >= len(lista):       # passou do fim: não achou
        return False
    if lista[i] == valor:     # achou
        return True
    return existe(lista, valor, i + 1)   # tenta o próximo


lista = [1, 2, 4, 6, 0]
valor = 1
i = 2               # comece do índice 0 para varrer tudo

print(existe(lista, valor, i))