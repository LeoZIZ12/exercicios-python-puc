def verificar_data(x):
    valido=True
    if len(x)!=10:
        valido=False
    for i in range (len(x)):
        if i==2 or i==5:
            if x[i]!="/":
                valido=False
        if i==3:
            if x[i]!="1":
                valido=False
        else:
            if "0">x[i] or x[i]>"9":
                valido=True
    return(valido)

def separar_data(x):
    dia_=""
    mes_=""
    ano_=""
    for i in range(len(x)):
        if i==0:
            dia_+=x[i]
        if i==1:
            dia_+=x[i]
        if i==3:
            mes_+=x[i]
        if i==4:
            mes_+=x[i]
        if i==6:
            ano_+=x[i]
        if i==7:
            ano_+=x[i]
        if i==8:
            ano_+=x[i]
        if i==9:
            ano_+=x[i]
    return int(dia_), int(mes_), int(ano_)

def verificar_bissexto(x):
    bissexto=False
    if x%400==0:
        bissexto=True
    if x%4==0 and x%100!=0:
        bissexto=True
    return bissexto

def verificar_dia_mes(x,y):
    dia_=True
    mes_=True
    if y<1 or y>12:
        mes_=False
    if x<1 or x>31:
        dia_=False
    if y==4 or mes==6 or mes==9 or mes==11:
        if x>30:
            dia_=False
    if y==2:
        if bissexto==True and x>30:
                dia_=False
        else:
            if bissexto==False and x>28:
                dia_=False
    return(dia_, mes_)
data=input("digite uma data(DD/MM/AAAA); ")
dia, mes, ano=separar_data(data)
bissexto=verificar_bissexto(ano)
print(ano)
print(verificar_data(data))
print(separar_data(data))
separar_data(data)
print(verificar_bissexto(ano))
print(verificar_dia_mes(dia, mes))