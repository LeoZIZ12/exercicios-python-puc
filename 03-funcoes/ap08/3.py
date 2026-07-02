def calcular_comissao(x):
    comissao=x * 0.05
    return(comissao)

valor_venda=int(input("Digite o valor da venda: "))
print(calcular_comissao(valor_venda))