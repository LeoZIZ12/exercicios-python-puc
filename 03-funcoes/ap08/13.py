def converter_tempo(x):
    tempo_horas=x//3600
    tempo_minutos=(x%3600)//60
    resto_segundos=(x%3600)%60
    tempo_convertido=f"{tempo_horas}Horas {tempo_minutos}Min {resto_segundos}seg"
    return(tempo_convertido)
def gerar_resumo_tempo(x,y):
    x=Nome_participante
    y=converter_tempo(y)
    print(f"Participante {x}:{y}")

Nome_participante=input("Digite o nome do participante: ")
tempo_segundos=int(input("Digite o tempo em segundo: "))

gerar_resumo_tempo(Nome_participante, tempo_segundos)