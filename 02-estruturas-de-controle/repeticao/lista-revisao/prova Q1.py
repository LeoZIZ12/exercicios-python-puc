#Temperatura
#Digitar -99 para parar
#Temperatura menor que zero ou maior que 500 é inválido
#Mais que três inválidos erro parar o código
#Para as Temperatura de 400 a 500 fazer a média 
#Indicar maior temperatura

temp=float(input("digite uma temperatura"))
contador=0
soma=0
invalidos=0

while temp >=0 and temp <=500:
    if temp>=400 and temp<=500:
        contador+=1
        soma+=temp
    temp_anterior=temp
    if temp>temp_anterior:
        maior=temp
    elif temp<temp_anterior:
        maior=temp_anterior
    if temp<0 or temp>500:
        print("numero invalido")
        invalidos+=1
if invalidos>3:
    print("Error:quantidade maxima de invalidos excedidos")
else:
    print(soma)
    print(maior)