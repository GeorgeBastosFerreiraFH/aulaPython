listaMotoristas = [
    {"nome": "João Silva", "idade": 34, "statusHabilitacao": True, "tipoHabilitacao": "A"},
    {"nome": "Maria Oliveira", "idade": 29, "statusHabilitacao": False, "tipoHabilitacao": "B"},
    {"nome": "Carlos Souza", "idade": 41, "statusHabilitacao": True, "tipoHabilitacao": "AB"},
    {"nome": "Fernanda Costa", "idade": 27, "statusHabilitacao": True, "tipoHabilitacao": "A"},
    {"nome": "Ricardo Pereira", "idade": 36, "statusHabilitacao": True, "tipoHabilitacao": "B"},
    {"nome": "Juliana Santos", "idade": 30, "statusHabilitacao": False, "tipoHabilitacao": "A"},
    {"nome": "Roberto Almeida", "idade": 50, "statusHabilitacao": True, "tipoHabilitacao": "AB"},
    {"nome": "Amanda Lima", "idade": 25, "statusHabilitacao": True, "tipoHabilitacao": "A"},
    {"nome": "Paulo Souza", "idade": 38, "statusHabilitacao": False, "tipoHabilitacao": "B"},
    {"nome": "Cláudia Martins", "idade": 33, "statusHabilitacao": True, "tipoHabilitacao": "AB"}
]


def exibirHabilitados(listaFuncionarios:list):
    for motoristaDaVez in listaFuncionarios:
        if motoristaDaVez["statusHabilitacao"] == True:
            print(f'O motorista {motoristaDaVez["nome"]} está apto para dirigir.')
        else:
            print(f'O motorista {motoristaDaVez["nome"]} não está apto para dirigir.')
        


def exibirPorTipo(listaFuncionarios:list):
    for motoristaDaVez in listaFuncionarios:
        if motoristaDaVez["tipoCarteira"] == 'A':
            print(f'O motorista {motoristaDaVez["nome"]} tem habilitação de categoria A')
        elif motoristaDaVez["tipoCarteira"] == 'B':
            print(f'O motorista {motoristaDaVez["nome"]} tem habilitação de categoria B')
        else:
            print(f'O motorista {motoristaDaVez["nome"]} tem habilitação de categoria AB')

def exibirPorIdade(listaFuncionarios:list):
    idade = int(input('Digite a idade para comparação: '))
    for motoristaDaVez in listaFuncionarios:
        if motoristaDaVez["idade"] <= idade:
            print(f'O motorista {motoristaDaVez["nome"]} possui {motoristaDaVez["idade"]} anos.')

exibirPorIdade(listaMotoristas)