class personagem:
    def __init__(self, nome,vida,ataque,defesa, pontos,x,y):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque
        self.defesa=defesa
        self.pontos=pontos
        self.x=x
        self.y=y
    def exibir(self):
        print(f"nome: {self.nome}")
        print(f"vida: {self.vida}")
        print(f"ataque: {self.ataque}")
        print(f"defesa: {self.defesa}")
        print(f"pontos: {self.pontos}")
        print(f"x: {self.x}")
        print(f"y: {self.y}")
    def mover(self,dx, dy):
        self.x+=dx
        self.y+=dy
    def coletar(self, item):
        self.pontos+=item.valor
        print(self.nome, "coletou", item.nome)

class inimigo:
    def __init__ (self,nome, vida, ataque, defesa, x, y):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque
        self.defesa=defesa
        self.x=x
        self.y=y
    def exibir(self):
        print(f"nome: {self.nome}")
        print(f"vida: {self.vida}")
        print(f"ataque: {self.ataque}")
        print(f"defesa: {self.defesa}")
        print(f"x: {self.x}")
        print(f"y: {self.y}")
    def mover(self,dx, dy):
        self.x+=dx
        self.y+=dy

class item:
    def __init__(self ,nome, valor, x, y):
        self.nome=nome
        self.valor=valor
        self.x=x
        self.y=y

p1= personagem("leo", 100, 10, 20, 0, 0, 0)
i1= inimigo("et", 20, 10, 5, 0, 0)
moeda= item("moeda", 10, 0, 0)

p1.exibir()
p1.coletar(moeda)
p1.exibir()