#pelo menos 8 carateres, pelo menos 1 numero, uma letra maiuscula, sem espaco

senha1="Leo190403"
senha2="leonardo"

def verificar_senha(senha):
    tamanho=0
    tem_numero=0
    for i in range (len(senha)):
        tamanho+=1
        if int(senha[i])>=0 or int(senha[i])<=9:
            tem_numero+=1
    if tamanho < 8:
        return False
    if tem_numero==0:
        return False
    return True

print(verificar_senha(senha1))
print(verificar_senha(senha2))

