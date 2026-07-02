dados=[]

def TratarLinha(linha):
    partes=linha.strip("\n").split(";")#strip tira ; split corta
    return partes[0], partes[1], partes[2]

with open("leituras.txt", "r") as arquivo: #abre e le o arquivo
    linhas=arquivo.readlines()#devolve um lista de linhas
    for linha in linhas:
        codigo, data, temp=TratarLinha(linha)
        dado=(codigo ,data ,temp)
        dados.append(dado)
print(dados)
Medicoes=0
Erros=0
total=0
maior=0
menor=0

for dado in dados:
    Medicoes+=1
    try:
        float(dado[2])
    except:
        Erros+=1
    else:
        total+=float(dado[2])
        if float(dado[2])>maior:
            maior=float(dado[2])

Medicoes_validas=Medicoes-Erros
media=total/Medicoes_validas
print("Medicoes validas: ",Medicoes_validas ,
      "media: ", media ,
      "maior: ", menor, 
      "menor: ", menor)