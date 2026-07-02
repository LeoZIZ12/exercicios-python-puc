produtos={

}
produto=str(input())
if produto!="fim":
    preco=float(input())
    produtos[produto]=preco
while produto!="fim":
    produto=str(input())
    if produto!="fim":
        preco=float(input())
        produtos[produto]=preco

print(produtos)