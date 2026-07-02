def converter_tempo(x):
    tempo_horas=x//3600
    tempo_minutos=(x%3600)//60
    resto_segundos=(x%3600)%60
    print(f"{tempo_horas}Horas {tempo_minutos}Min {resto_segundos}seg")

tempo_segundos=float(input("Digite o tempo em segundo: "))

converter_tempo(tempo_segundos)

