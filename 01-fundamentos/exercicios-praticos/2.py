salario=float(input("digite o salario minimo: "))
kw_gastos=int(input("Kw gastos: "))
kw_100=salario/7
kw_1=kw_100/100
valor_total=kw_1*kw_gastos
valor_com_desconto=valor_total*0.9

print(f"{kw_1:.2f}R$")
print(f"{valor_total:.2f}R$")
print(f"{valor_com_desconto:.2f}R$")