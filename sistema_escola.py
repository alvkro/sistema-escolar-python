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

class Turma():
    
    def __init__(self):
        self.turma = []

    def listar_aprovados(self):
        for aluno in self.turma:
            if aluno.nota >= 7.0:
                aluno.mostrar_info()

    def listar_reprovados(self):
            for aluno in self.turma:
                if aluno.nota < 7.0:
                    aluno.mostrar_info()

    #def maior_nota(self):
     #   top_nota = max(self.nota)
      #  print(f'A maior nota foi {top_nota}')

    def add_aluno(self):
        cad = int(input('Quantos alunos quer cadastrar? '))

        for cadastro in range(0, cad):
            nome = input('Digite o nome do aluno: \n')
            idade = int(input('Digite a idade desse aluno: \n'))
            nota = float(input('Digite a nota desse aluno: \n'))
            novo_aluno  = Aluno(nome, idade, nota)
            self.turma.append(novo_aluno)


    def show_turma(self): # Lista de alunos
        for aluno in self.turma:
            aluno.mostrar_info()
    
    def media_turma(self):
        soma_turma = 0
        for aluno in self.turma:
            soma_turma += aluno.nota
        m = soma_turma / len(self.turma)
        print(f'A média da turma foi {m:.2f}')

# Turmas da escola

turma1 = Turma('1A')

# Menu

while True:
    print('=== MENU ===')
    print('1 - Cadastrar Aluno')
    print('2 - Mostrar Alunos')
    print('3 - Média da Turma')
    print('0 - Sair')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        turma1.add_aluno()
    elif opcao == 2:
        turma1.show_turma()
    elif opcao == 3:
        turma1.media_turma()
    elif opcao == 0:
        print('Saindo do programa...')
        break
    else:
        print('Imput Inválido! Tente novamente. ')
