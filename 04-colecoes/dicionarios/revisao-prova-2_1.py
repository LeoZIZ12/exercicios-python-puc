loja = {
    "Arroz": 25.90,
    "Feijao": 9.50,
    "Macarrao": 6.99,
    "Leite": 5.49,
    "Cafe": 18.75
}


soma=0
qtd=0
for itens in loja.values():
    soma+=itens
    qtd+=1
    media=soma/qtd


mais_caro=0
for itens in loja.values():
    if itens>mais_caro:
        mais_caro=itens

mais_barato=25
for itens in loja.values():
    if itens<mais_barato:
        mais_barato=itens

acima_media=[]
for itens, valores in loja.items():
    if valores>media:
        acima_media.append(itens)




print(media)
print(mais_barato)
print(mais_caro)
print(acima_media)
    