estoque_inicial=1000
agricultores=0
def processar_pedido(x):
    pedido=int(input("digite"))
    global agricultores
    if pedido>x:
        return "pedido negado"
    else:
        x-=pedido
    while pedido >=0:
        pedido=int(input("digite"))
        if pedido>x:
            return "pedido negado"
        else:
            if x-pedido<=0:
                return "pedido negado"
            x-=pedido
        agricultores+=1
    return x, agricultores

processar_pedido(estoque_inicial)
estoque_final, agricultores=processar_pedido(estoque_inicial)
print(estoque_final,agricultores)