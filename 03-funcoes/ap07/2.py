Linhas=int(input("Digite um valor para Linhas"))
Colunas=int(input("Digite um valor para Colunas"))

def vefparouimpar():
    global produto, parouimpar
    if produto%2==0:
        parouimpar="par"
    else:
        parouimpar="Impar"
    return(parouimpar)

def veffaixa():
    global produto, faixa
    if produto <=10:
        faixa="pequeno"
    elif 11<=produto<=20:
        faixa="médio"
    elif produto>20:
        faixa="grande, maior q 20"
    return(faixa)

for i in range(1,Linhas+1):
    for j in range(1,Colunas+1):
        produto=i*j
        print (f"Linha {i} e Coluna {j}-> produto={produto}->{vefparouimpar()},{veffaixa()}")