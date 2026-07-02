def nome_aluno(x):
    print(f"O aluno {x}:")
def nota_valida(x):
    if 0<= x <=100:
        notavalida=True
    else:
        notavalida=False 
    return (notavalida)
def classificar_desempenho(x): 
    if 90<= x <-100:
        print("Excelente")
    elif 70<= x <=89:
        print("Bom")
    elif 60<= x <=69:
        print("Regular")
    elif x<60:
        print("Insuficiente")
def calcular_situacao(x):
    if x >=70:
        print ("Aprovado")
    elif 50<= x <=59:
        print ("Recuperacao")
    elif x<50:
        print ("Reprovado")


nome_aluno1=input ("Digite o nome do aluno: ")
nota1=int(input("Digite uma nota: "))

while nota_valida(nota1)==False:
    nota1=int(input("Digite uma nota valida(0-100): "))
if nota_valida(nota1)==True:
    print(nome_aluno1)
    print(f"nota={nota1}")
    print("A nota é valida")
    classificar_desempenho(nota1)
    calcular_situacao(nota1)