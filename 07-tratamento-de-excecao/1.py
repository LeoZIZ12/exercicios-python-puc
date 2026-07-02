try: #TENTE
    n=int(input("Digite um numero: "))
    Divisao=10/n
except ValueError: #tratamente para erro de valor
    print("Digite apenas numeros inteiros")
except ZeroDivisionError: #tratamento de valor==0
    print("nao e possivel diidir por 0")
else:#CASO N DE ERRO
    print(Divisao)
finally:#EXECUTA INDEPENDENTE DE ERRO OU N
    print("oi") 

#raise(gera error)

#EXCECOES MAIS COMUNS:
#ValueError (Valor incopativel)
#ZeroDivisionError (Divisao por 0)
#IndexError(posicao inexistente na lista)
#FileNotFoundError (Tentativa de abrir um arquivo que não existe.)
#TypeError (Operação incompatível com o tipo do dado)