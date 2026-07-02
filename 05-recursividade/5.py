def contar_digitos(x):
    global contador
    if x//10==0:
        contador+=1
        return contador
    else:
        contador+=1
        return contar_digitos(x//10)

contador=0
x=1234456
print(contar_digitos(x))