tupla=(4,10)

def maior_numero(tupla):
    maior=tupla[0]
    for valores in tupla:
        if valores>maior:
            maior=valores
    print(valores)

maior_numero(tupla)