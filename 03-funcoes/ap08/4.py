def calcular_valor_final(x,y):
    valor_desconto=(x/100)*y
    valor_final=x-valor_desconto
    return(valor_final)

valor_original=int(input("Digite o valor do produto: "))
percentual_desconto=int(input("digite o percentual de desconto: "))

print(calcular_valor_final(valor_original,percentual_desconto))