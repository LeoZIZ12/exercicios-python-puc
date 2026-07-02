senha=input("Digite a senha: ")
tentativas=0

while senha!="Leo190403" and tentativas < 3:
    senha= input("digite a senha novamente")
    tentativas= tentativas+1
if senha =="Leo190403":
    print("acesso permitido")
else:
    print("tentativas de vezes exedidas")