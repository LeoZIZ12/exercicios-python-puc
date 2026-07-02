indice_uv=float(input("digite o indice UV"))
if indice_uv<0:
    print("invalido")
elif indice_uv<3:
    print("baixo")
elif indice_uv<6:
    print("moderado")
elif indice_uv<8:
    print("alto")
elif indice_uv>=8:
    print("muito alto")