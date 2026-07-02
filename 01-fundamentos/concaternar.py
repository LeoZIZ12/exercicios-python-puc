Pin=" "
for contador in range (1,5):
    digito=input(f"digite o digito{contador}: ")
    while int(digito)<0 or int(digito)>9:
        digito=input(f"digito invalido, digite novamente o digito {contador}: ")
    Pin += digito
print(f"sua senha é {Pin}")