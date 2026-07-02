lista=[]
for i in range(5):
    n=input()
    lista.append(n)
    
i=len(lista)-1

with open("lista_invertida.txt", "w", encoding="utf-8") as arquivo:
    while i>=0:
        arquivo.write(lista[i]+"\n")
        i-=1