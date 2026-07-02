def exibir_cabecalho():
    print("Loja do Leo")
    print("Sistema de Atendimento")

def exibir_cliente():
    print(f"O nome do cliente é {nome_cliente}")

def calcular_comissao(x):
    comissao=x * 0.05
    return(comissao)

def calcular_valor_final(x,y):
    valor_desconto=(x/100)*y
    valor_final=x-valor_desconto
    return(valor_final)

exibir_cabecalho()
nome_cliente=input("Digite o nome do cliente: ")
exibir_cliente()
valor_produto=int(input("Digite o valor do produto: "))
print(f"A comissao será de {calcular_comissao(valor_produto)} R$")
percentual_desconto=int(input("digite o percentual de desconto: "))
print(f"O valor final com o desconto aplicado é de {calcular_valor_final(valor_produto,percentual_desconto)} R$")
