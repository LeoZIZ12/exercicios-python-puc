distancia_da_viagem=float(input("digite a distancia da viagem(km)"))
consumo_do_carro=float(input("digite o cosumo do seu veiculo(km/l)"))
preco_do_combustivel=6.03
litros_necessarios=distancia_da_viagem/consumo_do_carro
custo_estimado=litros_necessarios*preco_do_combustivel
print(f"{litros_necessarios:.2f}L")
print(f"{custo_estimado:.2f}R$")