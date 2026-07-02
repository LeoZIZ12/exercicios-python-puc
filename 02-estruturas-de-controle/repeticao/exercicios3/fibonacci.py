numero=int(input("digite nuemro"))
if numero <= 0:
    print("numero invalido")
else:
    a = 0
    b = 1
    i = 1

    while i <= numero:
        print(a, end=" ")
        c = a + b
        a = b
        b = c
        i = i + 1