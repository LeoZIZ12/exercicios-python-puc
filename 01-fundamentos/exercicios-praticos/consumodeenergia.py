potencia_aparelho=int(input("digite a potencia do aparelho"))
horas_de_uso=int(input("digite as horas de uso"))
dias_de_uso=int(input("digite os dias de uso"))
preco_da_energia=0.71
consumo_diario=potencia_aparelho*horas_de_uso
consumo_mensal=consumo_diario*dias_de_uso
custo_mensal=consumo_mensal*preco_da_energia
print(consumo_diario)
print(consumo_mensal)
print(custo_mensal)