valor_da_compra=float(input("digite o valor"))
percentual_de_imposto=float(input("digite o percentual"))
frete=float(input("digite o valor"))
valor_do_imposto=(percentual_de_imposto*valor_da_compra)/100
valor_total=valor_da_compra+valor_do_imposto+frete
print(f"{valor_do_imposto:.2f}R$")
print(f"{valor_total:.2f}R$1")