class aluno:
    def __init__(self, nome, mat, nota):
        self.nome=nome
        self.mat=mat
        self.nota=nota
    def exibir(self):
        print(f"nome:{self.nome}, Matricula:{self.mat}, Nota:{self.nota}")
    def alterar_nota(self,n):
        self.nota=n

a1=aluno("leo",908,0)

a1.alterar_nota(10)
a1.exibir()

