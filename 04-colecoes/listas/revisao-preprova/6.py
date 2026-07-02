numeros=[4,5,2,7]
alterna_par_impar=True
def alternou(x,y):
    if (x%2==0 and y%2!=0) or (x%2!=0 and y%2==0):
        return True
    return False

for i in range(1,len(numeros)):
    if not alternou(numeros[i],numeros[i-1]):
        alterna_par_impar=False
print(alterna_par_impar)

