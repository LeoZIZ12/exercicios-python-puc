filmes=[
    {
        "interestelar":10
    },
    {
        "pecadores":7.5
    },
    {
        "michael":6
    }
]

maior_nota=0
for chaves in filmes:
    for filme,nota in chaves.items():
        if nota>maior_nota:
            maior_nota=nota

menor_nota=maior_nota
soma=0
Contador=0
for chaves in filmes:
    for filmes, nota in chaves.items():
        if nota<menor_nota:
            menor_nota=nota
        soma+=nota
        Contador+=1

media=soma/Contador

print(maior_nota)
print(menor_nota)
print(media)


