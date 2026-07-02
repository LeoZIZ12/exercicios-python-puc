numero=int(input("digite um numero inteiro positiva: "))
cem=0
cinquenta=0
vinte=0
dez=0
cinco=0
um=0
while numero>0:
    if numero>100:
        numero-=100
        cem+=1
    elif numero <100 and numero>50:
        while numero>50:
            numero-=50
            cinquenta+=1
    elif numero<50 and numero>20:
        while numero>20:
            numero-=20
            vinte+=1
    elif numero<20 and numero>10:
        while numero>10:
            numero-=10
            dez+=1
    elif numero<10 and numero>5:
        while numero>5:
            numero-=5
            cinco+=1
    elif numero<5 and numero>1:
        while numero>1:
            numero-=1
            um+=1
print(f"cem{cem},cinquenta{cinquenta},vinte{vinte},dez{dez},cinco{cinco},um{um}")