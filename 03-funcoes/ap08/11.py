def calcular_inscricao(valor_base, taxa=10):
    return valor_base * (1 + taxa / 100)

valor_base = float(input("Digite o valor base da inscrição: R$ "))

total_taxa_padrao = calcular_inscricao(valor_base)
total_taxa_diferente = calcular_inscricao(valor_base, taxa=15)

print(f"\nCom taxa padrão (10%):  R$ {total_taxa_padrao:.2f}")
print(f"Com taxa diferente (15%): R$ {total_taxa_diferente:.2f}")
