conjunto1={1,2,3,4,5}
conjunto2={3,4,5,6,7}

def diferenca(conjunto1, conjunto2):
    diferenca=[]
    for numeros in conjunto1:
        if numeros not in conjunto2:
            diferenca.append(numeros)
    diferenca_conjunto=set(diferenca)
    print(diferenca_conjunto)

diferenca(conjunto1, conjunto2)