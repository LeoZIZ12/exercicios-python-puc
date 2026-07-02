lista_recuperada=[]

with open ("placas.txt", "r") as arquivo:
    for linha in arquivo:
        lista_recuperada.append(linha.strip())

print(lista_recuperada)