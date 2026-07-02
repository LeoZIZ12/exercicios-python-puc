lista=[1,2,3,4,5,5,5,6,7,8,9]

def conjunto_sem_repeticao(lista):
    sem_repetir=[]
    for valores in lista:
        if valores not in sem_repetir:
            sem_repetir.append(valores)
    conjunto_sem_repetir=set(sem_repetir)
    print(conjunto_sem_repetir)

conjunto_sem_repeticao(lista)