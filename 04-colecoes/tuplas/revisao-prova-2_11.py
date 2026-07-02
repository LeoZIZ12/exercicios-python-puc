lista=[("calca",100),("telefone",1000),("cueca",10),("carro",10000),("livro",60)]

def acima_100(lista):
    acima100=0
    for valores in lista:
        if valores[1]>100:
            acima100+=1
    print(acima100)

acima_100(lista)