tupla=("agua", "leo","amar","fresco", "Amor")

def comeca_a(tupla):
    contador=0
    for palavras in tupla:
        if palavras[0]=="a" or palavras[0]=="A":
            contador+=1
    print(contador)

comeca_a(tupla)
