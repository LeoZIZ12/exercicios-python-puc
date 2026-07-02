numero3digitos=int(input("digite um numero de 3 casas:"))
unidade=numero3digitos%(numero3digitos//10)
centena=numero3digitos//100
dezena=(numero3digitos-(centena*100+unidade))/10
invertido=unidade*100+dezena*10+centena
print(invertido)
