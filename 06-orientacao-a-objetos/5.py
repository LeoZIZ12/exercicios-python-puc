class cliente:
    def __init__(self,nome,matricula):
        self.nome=nome
        self.matricula=matricula
    def exibir_cliente(self):
        print("Cliente: ", self.nome)
        print("Matricula: ", self.matricula)

class produto:
    def __init__(self,nome,preco):
        self.nome=nome
        self.preco=preco
    def exibir_produto(self):
        print("produto: ", self.nome)
        print("preco: ", self.preco)

class item_pedido:
    def __init__(self, produto, quantidade):
        self.produto=produto
        self.quantidade=quantidade
    def cal_subtotal(self):
        Subtotal=self.produto.preco * self.quantidade
        return Subtotal
    def exibir_item_produto(self):
        print("produto: ", self.produto.nome)
        print("quantidade: ", self.quantidade)

class pedido:
    def __init__(self,numero, cliente): 
        self.numero=numero
        self.cliente=cliente
        self.itens=[]
    def adicionar_produto(self,produto, quantidade):
        item= item_pedido(produto, quantidade)
        self.itens.append(item)
    def valor_total(self):
        soma=0
        for item in self.itens:
            soma+=item.cal_subtotal()
        return soma
    def exibir_pedido(self):
        print("cliente: ", self.cliente.nome)
        print("pedido: ", self.numero)
        for item in self.itens:
            item.exibir_item_produto()
        print("valor total: ", self.valor_total())

ana= cliente("ana","1")
ana.exibir_cliente()
print()
sanduiche= produto("sanduiche", 18.50)
suco= produto("suco", 7.50)
pao_queijo= produto("Pao de queijo", 4.00)
print()
Pedido= pedido(1, ana)
Pedido.exibir_pedido()
print("--------------------------------")
Pedido.adicionar_produto(sanduiche, 2)
Pedido.adicionar_produto(suco, 2)
Pedido.exibir_pedido()



