base=int(input("digite uma base inteira positiva: "))
expoente=int(input("digite um expoente inteiro positivo: "))
resultado=1
for i in range(expoente):
    resultado*=base
print(resultado)