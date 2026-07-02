def criptografar(x):
    c_palavra=""
    if modo == "D":
        for letra in x:
            y=ord(letra)
            a=y+chave
            b=chr(a)
            c_palavra+=b
    elif modo == "E":
        for letra in x:
            y=ord(letra)
            a=y-chave
            b=chr(a)
            c_palavra+=b
    return(c_palavra)



palavra=input("digite uma palavra: ")
chave=int(input("digite um numero: "))
modo=input("Esquerda ou Direita: ")

print(f"{criptografar(palavra)}{modo}{chave}")