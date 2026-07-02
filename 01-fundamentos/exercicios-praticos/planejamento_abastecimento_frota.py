distancia_media_entrega=float(input("digite a distancia media das entregas(km)"))
numero_medio_entregas_dia=int(input("digite o numero medio de entregas/dia"))
numero_dias_na_semana=int(input("digite quantos dias de tabalho na semana"))
consumo_do_veiculo=float(input("digite o consumo do seu veiculo(km/L)"))
preco_do_combustivel=6.15
distancia_diaria=distancia_media_entrega*numero_medio_entregas_dia
distancia_semanal=distancia_diaria*numero_dias_na_semana
combustivel_necessario=distancia_semanal/consumo_do_veiculo
custo_semanal=combustivel_necessario*preco_do_combustivel
print(f"{distancia_diaria:.2f}Km")
print(f"{distancia_semanal:.2f}Km")
print(f"{combustivel_necessario:.2f}R$")
print(f"{custo_semanal:.2f}R$")