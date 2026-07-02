def calcular_preco_cafe(x,y=0):
    preco_total=x+y
    return preco_total

def resumo_item(x,y):
    resumo=f"{x}:{y}R$"
    return resumo

def calcular_totais(x,y,taxa=10):
    subtotal=x+y
    taxa_=(subtotal/100)*taxa
    total=subtotal+taxa_
    print(subtotal,taxa_,total)
    