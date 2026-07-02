nomedofuncionario=str(input("Qual seu nome?"))
salariobase=float(input("seu salario:"))
percentualdebonus=float(input("percentual:"))
valorbonificado=(salariobase*(percentualdebonus*0.01))+salariobase
print(nomedofuncionario)
print(f"{salariobase:.2f}R$")
print(f"{percentualdebonus:.2f}%")
print(f"{valorbonificado:.2f}R$")