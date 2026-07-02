def contar_vogais(texto,i):
    global vogal
    if i==len(texto):
        return vogal
    elif texto[i] in "aeiouAEIOU":
        vogal+=1
    return contar_vogais(texto,i+1)

vogal=0
texto="banana"

print(contar_vogais(texto,0))