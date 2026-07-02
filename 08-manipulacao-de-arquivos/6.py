def Tratar_linhas(linha):
    partes = linha.strip("\n").split(";")
    return partes[0], partes[1], partes[2], partes[3], partes[4]
def vef_resultado(aluno):
    soma=int(aluno[2])+int(aluno[3])+int(aluno[4])
    media=soma/3
    if media>=70:
        return "Aprovado", media
    if media >=40 and media<70:
        return "Exame esepecial", media
    if media <40:
        return "Reprovado", media


lista = []
with open("notas.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)
    for linha in linhas:
        matricula, nome, nota1, nota2, nota3 = Tratar_linhas(linha)
        tupla = (matricula, nome, nota1, nota2, nota3)
        lista.append(tupla)

print(lista)

lista2=[]
with open("resultado.txt", "w") as arquivo :
    for aluno in lista:
        resultado, media=vef_resultado(aluno)
        arquivo.write(f"{aluno[0]};{aluno[1]};{media};{resultado}\n")
        tupla2=(aluno[0], media, resultado)
        lista2.append(tupla2)

print(lista2)