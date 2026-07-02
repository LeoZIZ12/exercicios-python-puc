def ler_nota(nota):
    if int(nota)<0 or int(nota)>100:
        raise ValueError("Nota fora do intervalo")
    
i=0
lista=[]
while i<3:
    aluno_nome=str(input("digite o nome: "))
    try:
        aluno_nota=int(input("digite a nota(entre 0 e 100): "))
        ler_nota(aluno_nota)
    except ValueError as erro:
        print("Erro: ", erro)
    except ValueError:
        print("Digite apenas numeros inteiros")
    else:
        tupla=(aluno_nome,aluno_nota)
        lista.append(tupla)
        i+=1

print(lista)