listaTarefas = dict()

def adicionarTarefas():
    tarefaNome = input('\nDigite o nome da tarefa: ')
    descricao = input('Digite a descrição da tarefa: ')
    prioridade = int(input('Digite a prioridade da tarefa (escala de 1-5): '))
    categoria = input('Qual a categoria da tarefa: ')

    listaTarefas[tarefaNome] = {
        'Nome': tarefaNome,
        'Descrição': descricao,
        'Prioridade': prioridade,
        'Categoria': categoria,
        'Concluida': '[ ]'
    }

    print(f'\nTarefa {tarefaNome} cadastrada com sucesso!\n')

def exibirTarefas():
    if not listaTarefas:
        print('\nNenhuma tarefa.')

    for contador,(nome, dados) in enumerate(listaTarefas.items(), start=1):
        print(f'\n{contador}º tarefa\n')
        print(f'Nome: {dados['Nome']}')
        print(f'Descrição: {dados['Descrição']}')
        print(f'Prioridade: {dados['Prioridade']}')
        print(f'Categoria: {dados['Categoria']}')
        print(f'Concluida: {dados['Concluida']}')

def marcarTarefaConcluida():
    if not listaTarefas:
            print('\nNenhuma tarefa.')
    else:
        exibirTarefas()
        tarefaConcluida = int(input('\nDigite a colocação da tarefa concluída: '))
        for contador, (nome, dados) in enumerate(listaTarefas.items(), start=1): 
            if contador == tarefaConcluida: 
                dados['Concluida'] = '[X]' 
                print(f'\nTarefa {nome} marcada como concluída!') 
                tarefa_encontrada = True 
                break
            
        if not tarefa_encontrada: 
            print('Tarefa não encontrada.')


def exibirPrioridade():
    if not listaTarefas:
        print('\nNenhuma tarefa.')

    tarefasPrioridade = sorted(listaTarefas.items(), key=lambda x: x[1]['Prioridade']) 
    for contador, (nome, dados) in enumerate(tarefasPrioridade, start=1): 
        print(f'\n{contador}º tarefa (Prioridade: {dados["Prioridade"]})\n') 
        print(f'Nome: {dados["Nome"]}') 
        print(f'Descrição: {dados["Descrição"]}') 
        print(f'Categoria: {dados["Categoria"]}') 
        print(f'Concluida: {dados["Concluida"]}')

def exibirCategoria():
    if not listaTarefas:
        print('\nNenhuma tarefa.')

    tarefasCategoria = sorted(listaTarefas.items(), key=lambda x: x[1]['Categoria'])
    for contador, (nome, dados) in enumerate(tarefasCategoria, start=1):
        print(f'\n{contador}º tarefa (Categoria: {dados["Categoria"]})\n')
        print(f'Nome: {dados["Nome"]}') 
        print(f'Descrição: {dados["Descrição"]}') 
        print(f'Prioridade: {dados["Prioridade"]}') 
        print(f'Concluida: {dados["Concluida"]}')

def removerTarefa():
    if not listaTarefas:
            print('\nNenhuma tarefa.')
    else:
        exibirTarefas()
        tarefaRemover = int(input('\nDigite a colocação da tarefa a ser removida: '))
        
        if 1 <= tarefaRemover <= len(listaTarefas): 
            tarefa = list(listaTarefas.keys()) 
            tarefa = tarefa[tarefaRemover - 1] 
            del listaTarefas[tarefa] 
            print(f'\nTarefa "{tarefa}" removida com sucesso!') 
        else: 
            print('\nTarefa não encontrada.')

while True:
    continuar = input("""
    1 - Cadastrar tarefa
    2 - Listar tarefas
    3 - Marcar tarefa como concluída
    4 - Exibir as tarefas por prioridade
    5 - Exibir as tarefas por categoria
    6 - Apagar Tarefa
    0 - Sair

    """)
    if continuar == '1':
        adicionarTarefas()
        
    elif continuar == '2':
        exibirTarefas()
    elif continuar == '3':
        marcarTarefaConcluida()
    elif continuar == '4':
        exibirPrioridade()
    elif continuar == '5':
        exibirCategoria()
    elif continuar == '6':
        removerTarefa()
    elif continuar == '0':
        print("Programa encerrado!")
        break
    else:
        print('Opção inválida. Digite alguma opção do menu')
