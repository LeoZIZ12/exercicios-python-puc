def converter_para_lista(x):
    lista_convetida=[]
    for letras in x:
        lista_convetida.append(letras)
    return lista_convetida

palavras=str(input(""))
print(converter_para_lista(palavras))