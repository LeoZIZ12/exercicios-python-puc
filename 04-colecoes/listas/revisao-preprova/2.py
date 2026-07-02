numeros=[1,2,3,4,5,6,7,8,9,10]
soma=0
for numero in numeros:
    soma+=numero

media=soma/len(numeros)

def verificar_maior_que_media():
    numeros_maior_que_media=[]
    for numero in numeros:
        if numero>media:
            numeros_maior_que_media.append(numero)
    return numeros_maior_que_media

print(verificar_maior_que_media())
