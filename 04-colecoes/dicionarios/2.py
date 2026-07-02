produto = {
    "nome": "mouse",
    "preco": 120,
    "estoque": 5
}

for chaves in produto:
    print(chaves)

for valores in produto:
    print(produto[valores])

for chaves, valores in produto.items():
    print(produto.items())