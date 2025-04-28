# Sistema de cadastro de alunos:

class Aluno():

    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def mostrar_info(self):
        print(f'Nome: {self.nome}; Idade: {self.idade}; Nota: {self.nota}')

    def status_aprovado(self):
        if self.nota >= 7.0:
            print(f'{self.nome} foi APROVADO')
        else:
            print(f'{self.nome} foi REPROVADO')

lista_alunos = []

# Sistema de cadastro de alunos

cad = int(input('Quantos alunos quer cadastrar? '))

for cadastro in range(0, cad):
    nome = input('Digite o nome do aluno: \n')
    idade = int(input('Digite a idade desse aluno: \n'))
    nota = float(input('Digite a nota desse aluno: \n'))

    novo_aluno = Aluno(nome, idade, nota)
    lista_alunos.append(novo_aluno)

for aluno in lista_alunos:
    aluno.mostrar_info()
    aluno.status_aprovado()
    print('-------')