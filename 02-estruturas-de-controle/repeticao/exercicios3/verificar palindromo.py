Palavra=str(input("digite uma palavra: "))
palavra_invertida=""
for letra in Palavra:
    palavra_invertida=letra+palavra_invertida
if palavra_invertida==Palavra:
    print(f"{Palavra} é palindromo pois ela ao contrario é {palavra_invertida}")
else:
    print(f"{Palavra} nao é um palindromo pois ela ao contrario é {palavra_invertida}")