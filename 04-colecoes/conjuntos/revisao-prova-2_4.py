conjunto1={1,2,3,4,5}
conjunto2={3,4,5,6,7}

def intercecao(conjunto1, conjunto2):
    intercecao=[]
    for numeros1 in conjunto1:
        for numeros2 in conjunto2:
            if numeros1==numeros2:
                intercecao.append(numeros1)
    conjunto_intercecao=set(intercecao)
    print(conjunto_intercecao)

intercecao(conjunto1, conjunto2)



