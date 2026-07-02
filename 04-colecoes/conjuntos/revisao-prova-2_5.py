conjunto1={1,2,3,4,5}
conjunto2={3,4,5,6,7}

def uniao(conjunto1, conjunto2):
    uniao=[]
    for numeros1 in conjunto1:
        if numeros1 not in uniao:
            uniao.append(numeros1)
    for numeros2 in conjunto2:
        if numeros2 not in uniao:
            uniao.append(numeros2)
    conjunto_uniao=set(uniao)
    print(conjunto_uniao)

uniao(conjunto1, conjunto2)
