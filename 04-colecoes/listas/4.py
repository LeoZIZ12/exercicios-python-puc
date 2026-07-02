jogadas=[]
for i in range(5):
    jogada=int(input(""))
    jogadas.append(jogada)

media=sum(jogadas)/len(jogadas)
acima=[]
abaixo=[]

for valores in jogadas:
    if valores >= media:
        acima.append(valores)
    if valores<media:
        abaixo.append(valores)
print(acima)
print(abaixo)