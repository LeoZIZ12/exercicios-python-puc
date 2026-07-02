A=int(input("Digite um valor para A"))
B=int(input("Digite um valor para B"))

def vefmultiplo3():
  global i
  if i%3==0:
    print(f"{i}-multiplo de 3")
    
def vefmultiplo5():
  global i
  if i%5==0:
    print(f"{i}-multiplo de 5")

def vefmultiploambos():
  global i
  if i%15==0:
    print(f"{i}-multiplo de ambos")

def vefnenhum():
  global i
  if i%3!=0 and i%5!=0 and i%15!=0:
    print(f"{i}-nenhum")

for i in range (A,B):
  vefmultiplo3()
  vefmultiplo5()
  vefmultiploambos()
  vefnenhum()

