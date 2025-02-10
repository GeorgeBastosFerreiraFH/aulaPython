class Tarefa():
    def __init__(self, nome, data, prioridade):
        self.nome = nome
        self.data = data
        self.prioridade = prioridade
        self.projeto = None

    def associar_projeto(self, projeto):
        self.projeto = projeto

    def __str__(self):
        return f"Nome: {self.nome} - Data: {self.data} - Prioridade: {self.prioridade}"

class Projeto():
    def __init__(self, nomeProjeto, status):
        self.nomeProjeto = nomeProjeto
        self.status = status
        self.tarefas = []
    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)
        tarefa.associar_projeto(self)
    
    def listar_tarefas(self):
        if not self.tarefas:
            return f"Não há tarefas para o projeto {self.nomeProjeto}"
        
        return f"\n".join(str(tarefa) for tarefa in self.tarefas)
    
    def __str__(self):
        return f"Projeto {self.nomeProjeto}"
    

# Criando algumas tarefas
tarefa1 = Tarefa("Finalizar relatório de vendas", "15-02-2025", "Alta")
tarefa2 = Tarefa("Reunião de planejamento", "12-02-2025", "Média")
tarefa3 = Tarefa("Estudar novas tecnologias", "20-02-2025", "Baixa")
tarefa4 = Tarefa("Revisar orçamento do projeto", "14-02-2025", "Alta")

# Criando um projeto
projeto1 = Projeto("Desenvolvimento de Website", "Em andamento")

# Associando tarefas ao projeto
projeto1.adicionar_tarefa(tarefa1)
projeto1.adicionar_tarefa(tarefa2)
projeto1.adicionar_tarefa(tarefa3)
projeto1.adicionar_tarefa(tarefa4)

# Exibindo o projeto e as tarefas associadas a ele
print(f"Projeto: {projeto1}")
print(projeto1.listar_tarefas())
