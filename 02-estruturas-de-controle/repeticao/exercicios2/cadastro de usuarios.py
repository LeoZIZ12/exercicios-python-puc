#usuario1
usuario1=str(input("digite seu nome: "))
letras= len(usuario1)
while letras<3:
    usuario1=str(input("digite seu nome novamente: "))
    letras= len(usuario1)

vogais = "aeiou" 
contador_de_vogais1=0
for letras in usuario1:
    if letras in vogais:
        contador_de_vogais1=contador_de_vogais1+1

print(f"usuario1:{usuario1}")
print(f"vogais:{contador_de_vogais1}")

#usuario2
usuario2=str(input("digite seu nome: "))
letras= len(usuario1)
while letras<3:
    usuario2=str(input("digite seu nome novamente: "))
    letras= len(usuario2)

vogais = "aeiou" 
contador_de_vogais2=0
for letras in usuario2:
    if letras in vogais:
        contador_de_vogais2=contador_de_vogais2+1

print(f"usuario2:{usuario2}")
print(f"vogais:{contador_de_vogais2}")

#usuario3
usuario3=str(input("digite seu nome: "))
letras= len(usuario1)
while letras<3:
    usuario3=str(input("digite seu nome novamente: "))
    letras= len(usuario3)

vogais = "aeiou" 
contador_de_vogais3=0
for letras in usuario1:
    if letras in vogais:
        contador_de_vogais3=contador_de_vogais3+1

print(f"usuario3:{usuario3}")
print(f"vogais:{contador_de_vogais3}")

#usuario4
usuario4=str(input("digite seu nome: "))
letras= len(usuario1)
while letras<3:
    usuario4=str(input("digite seu nome novamente: "))
    letras= len(usuario2)

vogais = "aeiou" 
contador_de_vogais4=0
for letras in usuario4:
    if letras in vogais:
        contador_de_vogais4=contador_de_vogais4+1

print(f"usuario4:{usuario4}")
print(f"vogais:{contador_de_vogais4}")

#usuario5
usuario5=str(input("digite seu nome: "))
letras= len(usuario5)
while letras<3:
    usuario5=str(input("digite seu nome novamente: "))
    letras= len(usuario5)

vogais = "aeiou" 
contador_de_vogais5=0
for letras in usuario5:
    if letras in vogais:
        contador_de_vogais5=contador_de_vogais5+1

print(f"usuario5:{usuario5}")
print(f"vogais:{contador_de_vogais5}")