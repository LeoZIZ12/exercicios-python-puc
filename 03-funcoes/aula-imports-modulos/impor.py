import util_data
data=input("digite uma data(DD/MM/AAAA); ")

util_data.verificar_data(data)

dia, mes, ano = util_data.separar_data(data)
print(dia, mes, ano)
