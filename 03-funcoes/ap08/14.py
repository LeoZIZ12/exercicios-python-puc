def eh_par(x):
    par=""
    if x%2==0:
        par=True
    else:
        par=False
    return(par)

def contar_pares_faixa(x):
    contador=0
    for letras in str(x):
        if eh_par(int(letras))==True:
            contador+=1
    print(f"A quantida de numeros pares é igual a: {contador}")
        

faixa_numerica=int(input("Digite a faixa: "))

contar_pares_faixa(faixa_numerica)