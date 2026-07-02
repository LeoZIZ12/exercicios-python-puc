numero=int(input("digite um numero"))
if numero <=0:
    print("numero invalido")
else:
    fatorial = 1
    i = 1
    
    while numero >=i:
        fatorial = fatorial * i
        i = i + 1
    
    print("O fatorial de", numero, "é", fatorial)