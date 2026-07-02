def classifcar_prato(prato, criterio):
    if prato[1]>=criterio[0] and prato[2]>=criterio[1]:
        return(True)

min_sabor=input("digite a nota minima de sabor: ")
min_apresentacao=input("digite a nota minima de apresentacao: ")
criterio=(min_sabor, min_apresentacao)

classificados=[]
qtd=0

nome=input("digite o nome do prato: ")
if nome!="sair":
    nota_sabor=input("digite a nota do sabor do prato: ")
    nota_apresentacao=input("digite a nota da apresentacao do prato: ")
    pratos=(nome, nota_sabor, nota_apresentacao)
    if classifcar_prato(pratos, criterio):
        classificados.append(pratos[0])
        qtd+=1
while nome != "sair":
    nome=input("digite o nome do outro prato: ")
    if nome!="sair":
        nota_sabor=input("digite a nota do sabor do outro prato: ")
        nota_apresentacao=input("digite a nota da apresentacao do outro prato: ")
        pratos=(nome, nota_sabor, nota_apresentacao)
        if classifcar_prato(pratos, criterio):
            classificados.append(pratos[0])
            qtd+=1

if qtd==0:
    print("nenhum prato classificado")
elif qtd>1:
    print("pratos classificados:", classificados)
    print("total:", qtd)