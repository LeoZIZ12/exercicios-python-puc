codigos=[3, 7, 6]
for i in range (1,len(codigos)):
    crescente=True
    if codigos[i-1] >= codigos[i]:
        crescente=False

print(crescente)