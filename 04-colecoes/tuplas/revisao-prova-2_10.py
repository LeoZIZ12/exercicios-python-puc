lista=[("pedro",1),("leo",2),("gui",10)]

def maior_nota(lista):
    maior_aluno=""
    maior=0
    for aluno in lista:
        if aluno[1]>maior:
            maior_aluno=aluno[0]
            maior=aluno[1]
    print(maior_aluno)

maior_nota(lista)