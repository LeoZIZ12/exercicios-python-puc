class personagem:
    def __init__(self, nome,vida):
        self.nome=nome
        self.vida=vida
        self.inventario=inventario()
    def exibir(self):
        print(f"nome: {self.nome}")
        print(f"vida: {self.vida}")
        print(f"inventario: {inventario.exibir_inventario()}")
    def coletar(self, item):
        self.inventario.adicionar_item(item)
        print(self.nome, "coletou", item.nome)

class inventario:
    def __init__(self):
        self.itens=[]
    def adicionar_item(self,item):
        self.itens.append(item)
    def exibir_inventario(self):
        for item in self.itens:
            print(f"item: {self.nome}, Valor: {self.valor},")
        
class item:
    def __init__(self ,nome, valor):
        self.nome=nome
        self.valor=valor


inventario1= inventario()
p1= personagem("leo", 100)
moeda= item("moeda", 10)
agua= item("agua", 2)

p1.exibir()
inventario1.exibir_inventario()

p1.coletar(moeda)

inventario1.exibir_inventario()