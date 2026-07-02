placas=[1234, 5678, 4567, 7543]

with open("placas.txt", "w")as arquivo:
    for placa in placas:
        arquivo.write(str(placa) + "\n")
