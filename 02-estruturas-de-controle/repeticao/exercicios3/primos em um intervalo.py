i_intevalo=int(input("digite o inicio do intervalo: "))
f_intervalo=int(input("digite o fim do intervalo: "))

for numero in range(i_intevalo, f_intervalo + 1):
    if numero > 1:
        divisores = 0
        
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores += 1
        
        if divisores == 2:
            print(numero)