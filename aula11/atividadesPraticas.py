# Atividade 01

class Cachorro:
    def __init__(self, nome, raça, idade):
        self.nome = nome
        self.raça = raça
        self.idade = idade

# Atividade 02

class Pessoa:
    def __init__(self, nome, idade, peso, gênero):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.gênero = gênero

# Atividade 03

class Empresa:
    def __init__(self):
        self.funcionarios = []
    
    def adicionar_funcionario(self, nome, cargo, salario):
        funcionario = {
            'nome': nome,
            'cargo': cargo,
            'salario': salario
        }
        self.funcionarios.append(funcionario)
        print(f'Funcionario {nome} adicionado com sucesso!')

    def remover_funcionario(self, nome):
        if not self.funcionarios:
            print('Nenhum funcionario encontrado!')
        
        for funcionario in self.funcionarios:
            if funcionario['nome'] == nome:
                self.funcionario.remove(funcionario)
                print(f'Funcionario {nome} removido com sucesso!')
            else:
                print(f'Funcionario {nome} não encontrado!')
    
    def listar_funcionarios(self):
        if not self.funcionarios:
            print('Nenhum funcionario encontrado!')

        if self.funcionarios:
            print("\n---------------------")
            print("Funcionários da empresa:")
            print("---------------------\n")
            for funcionario in self.funcionarios:
                print(f'Nome: {funcionario["nome"]}')
                print(f'Cargo: {funcionario["cargo"]}')
                print(f'Salario: {funcionario["salario"]}')
                print('------------------------\n')

empresa = Empresa()
             
empresa.adicionar_funcionario(nome="George Bastos", cargo="Desenvolvedor FullStack", salario=5000)
empresa.listar_funcionarios()