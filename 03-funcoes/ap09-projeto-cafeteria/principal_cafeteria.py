import funcoes_cafeteria_leo
Nome_item=input("Digite o item: ")
preco_base=float(input("Digite o preco base do item: "))
Nome_acompanhamento=input("Digite o acompanhamento: ")
acrescimo=float(input("Digite o preco do acrescimo:"))
Nome_item2=input("Digite o item2: ")
preco_base2=float(input("Digite o preco base do item2: "))
Nome_acompanhamento2=input("Digite o acompanhamento: ")
acrescimo2=float((input("Digite o preco do acrescimo:")))

preco_total=(funcoes_cafeteria_leo.calcular_preco_cafe(preco_base, acrescimo))
preco_total2=(funcoes_cafeteria_leo.calcular_preco_cafe(preco_base2, acrescimo2))

resumo=funcoes_cafeteria_leo.resumo_item(Nome_item,preco_total)
resumo2=funcoes_cafeteria_leo.resumo_item(Nome_item2,preco_total2)

print(resumo, resumo2)