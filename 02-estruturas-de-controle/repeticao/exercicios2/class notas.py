nota=float(input("digite uma nota:"))
otimo=0
bom=0
regular=0
insatisfatorio=0
while nota>=0 and nota<=10:
    if nota >=8 and nota<=10:
        otimo=otimo+1
    elif nota >=7 and nota <8:
        bom=bom+1
    elif nota>=5 and nota<7:
        regular=regular+1
    elif nota<5:
        insatisfatorio=insatisfatorio+1
    nota=float(input("digite uma nova nota:"))
if nota <0 or nota >10:
    print("otimo=", otimo)
    print("bom=", bom)
    print("insatisfatorio=", insatisfatorio)