paginas_do_livro=int(input("qntd paginas do livro"))
numero_medio_palavras_pagina=int(input("numero medio palavras por pagina"))
velocidade_media_palavras_por_minuto=int(input("velocidade medua de palavras lidas por minuto"))
qtd_minutos_disponiveis_por_dia=int(input("quantidade de mintos disponiveis por dia"))
numero_palavras_livro=paginas_do_livro*numero_medio_palavras_pagina
tempo_total_de_leitura_minutos=numero_palavras_livro/velocidade_media_palavras_por_minuto
tempo_total_de_leitura_horas=tempo_total_de_leitura_minutos/60
dias_estimados=tempo_total_de_leitura_horas/24
print(numero_palavras_livro)
print(tempo_total_de_leitura_minutos)
print(f"{tempo_total_de_leitura_horas:.2f}horas")
print(f"{dias_estimados:.2f}dias")