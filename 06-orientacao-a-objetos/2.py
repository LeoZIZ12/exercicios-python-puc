class personagem:
    def __init__(self, nome,vida,ataque,defesa,x,y):
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
        
p1 = personagem("leo",100,10,50,0,0)

p1.exibir()
p1.mover(10,50)
p1.exibir()