def calcular_inscricao(valor_base, taxa=10):
    return valor_base * (1 + taxa / 100)
def converter_tempo(x):
    tempo_horas=x//3600
    tempo_minutos=(x%3600)//60
    resto_segundos=(x%3600)%60
    tempo_convertido=f"{tempo_horas}Horas {tempo_minutos}Min {resto_segundos}seg"
    return(tempo_convertido)
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
    return(contador)

Nome_participante=input("Digite o nome do participante: ")
valor_base = float(input("Digite o valor base da inscrição: "))
tempo_segundos=int(input("Digite o tempo em segundo: "))
faixa_numerica=int(input("Digite a faixa: "))

print(f"Dados participante {Nome_participante}: \nValor da inscricao:{calcular_inscricao(valor_base, taxa=10):.2f}R$ \nTempo de prova{converter_tempo(tempo_segundos)} \nNumero pares na faixa:{contar_pares_faixa(faixa_numerica)}")
