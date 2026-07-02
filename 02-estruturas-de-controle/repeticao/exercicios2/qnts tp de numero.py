n=int(input("digite um numero:"))
positivos=0
negativos=0
pares=0
impares=0
while n!=0:
    if n>0:
        positivos=positivos+1 
    elif n<0:
        negativos=negativos+1

    if n%2==0:
        pares=pares+1
    elif n%2!=0 and n%2>0:
        impares=impares+1
    n=int(input("digite um numero novamente:"))
if n==0:
    print("positivos=", positivos)
    print("negativos=", negativos)
    print("pares=", pares)
    print("impares=", impares)

