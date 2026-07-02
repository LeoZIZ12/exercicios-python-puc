valor_add= float(input("Digite o valor: "))
compra=0

while valor_add!=0:
    if valor_add<0:
        print("valor invalido")
    else:
        compra=compra+valor_add
    valor_add= float(input("digite mais um valor: "))
if compra>0:
    if compra>=200:
        print("voce ganhou frete grátis!")
    else:
        print("frete normal")
print(compra)
