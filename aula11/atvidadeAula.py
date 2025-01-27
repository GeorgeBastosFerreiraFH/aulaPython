# Atividade 01

motoristas = dict()

def cadastrarMotorista():
    nome = input('Digite o nome do motorista: ')
    idade = input('Digite a idade do motorista: ')
    statusHabilitacao = input('Digite o status da habilitação (1 - Apto / 2 - Inapto): ')
    tipoHabilitacao = input('Digite o tipo da Habilitação (A/B ou AB): ').lower()

    motoristas[nome]= {
        'nome': nome,
        'idade': idade,
        'statusHabilitacao': statusHabilitacao,
        'tipoHabilitacao': tipoHabilitacao
    }

    print(f'O motorista {nome} foi cadastrado com sucesso!')

def exibirMotoristaAptoOuInapto():
    if not motoristas:
        print('Não há motoristas cadastrados!')

    
    for nome, dados in motoristas.items():
        if motoristas[nome]['statusHabilitacao'] == '1':
            status = 'Apto'
            print(f'Nome: {dados['nome']}')
            print(f'Idade: {dados['idade']} anos')
            print(f'Status da Habilitação: {status}')
            print(f'Tipo da Habilitação: {dados["tipoHabilitacao"]}')
        else:
            status = 'Inapto'
            print(f'Nome: {dados['nome']}')
            print(f'Idade: {dados['idade']} anos')
            print(f'Status da Habilitação: {status}')
            print(f'Tipo da Habilitação: {dados["tipoHabilitacao"]}')

def exibirMotoristaTipoHabilitacao():
    if not motoristas:
        print('Não há motoristas cadastrados!')

    for nome, dados in motoristas.items():
        if dados['tipoHabilitacao'] == 'a':
            print('\n----------------------------')
            print(f'Motoristas com habilitação A')
            print('----------------------------\n')
            print(f'Nome: {dados['nome']}')
            print(f'Idade: {dados['idade']} anos')
            print(f'Status da Habilitação: {dados["statusHabilitacao"]}')
            print(f'Tipo da Habilitação: {dados["tipoHabilitacao"]}')

        elif dados['tipoHabilitacao'] == 'b':
            print('\n----------------------------')
            print(f'Motoristas com habilitação B')
            print('----------------------------\n')
            print(f'Nome: {dados['nome']}')
            print(f'Idade: {dados['idade']} anos')
            print(f'Status da Habilitação: {dados["statusHabilitacao"]}')
            print(f'Tipo da Habilitação: {dados["tipoHabilitacao"]}')

        elif dados['tipoHabilitacao'] == 'ab':
            print('\n----------------------------')
            print(f'Motoristas com habilitação AB')
            print('----------------------------\n')
            print(f'Nome: {dados['nome']}')
            print(f'Idade: {dados['idade']} anos')
            print(f'Status da Habilitação: {dados["statusHabilitacao"]}')
            print(f'Tipo da Habilitação: {dados["tipoHabilitacao"]}')

        else:
            print('\n----------------------------')
            print(f'Motoristas com outros tipos de Habilitação')
            print('----------------------------\n')
            print(f'Nome: {dados['nome']}')
            print(f'Idade: {dados['idade']} anos')
            print(f'Status da Habilitação: {dados["statusHabilitacao"]}')
            print(f'Tipo da Habilitação: {dados["tipoHabilitacao"]}')

def exibirMotoristaIdade():
    if not motoristas:
        print('Não há motoristas cadastrados!')

    for nome, dados in motoristas.items():
        idadeComparar = int(input('Exiba os motoristas com idade maior que: '))

        if dados['idade'] > idadeComparar:
            print('\n----------------------------')
            print(f'Motoristas com idade maior que {idadeComparar} anos')
            print('----------------------------\n')
            print(f'Nome: {dados['nome']}')
            print(f'Idade: {dados["idade"]} anos')
            print(f'Status da Habilitação: {dados["statusHabilitacao"]}')
            print(f'Tipo da Habilitação: {dados["tipoHabilitacao"]}')
        elif idadeComparar <= 0:
            print('Idade inválida! Digite um número positivo')
        else:
            print('Não há motoristas com idade maior que a informada!')

def exibirMenu():
     print("""
    -------------------------
    1 - Cadastrar motorista
    2 - Exibir motoristas Aptos/Inaptos
    3 - Exibir motoristas tipo de habilitação
    4 - Exibir motoristas com idade maior que
    0 - Sair
    -------------------------
    
    Opção: """)

        
def main():

    while True:
        exibirMenu()
        
        opcao = input()


        if opcao == '0':
            print('\n----------------------')
            print('Programa encerrado')
            print('----------------------\n')
            break

        elif opcao == '1':
            cadastrarMotorista()
        elif opcao == '2':
            exibirMotoristaAptoOuInapto()
        elif opcao == '3':
            exibirMotoristaTipoHabilitacao()
        elif opcao == '4':
            exibirMotoristaIdade()
            break
        else:
            print('Opção inválida! Tente novamente.')

if __name__ == "__main__":
    main()


# Atividade 02

class Celular():
    def __init__(self, marca, modelo, polegadas, armazenamento, mem_ram):
        self.marca = marca
        self.modelo = modelo
        self.polegadas = polegadas
        self.armazenamento = armazenamento
        self.mem_ram = mem_ram
        self.status_celular = False
        self.status_chamada = False

    def ligar(self):
        if self.status_celular:
            print('O celular já está ligado!')
        else:
            self.status_celular = True
            print('O celular está ligado!')
    
    def desligar(self):
        if self.status_celular:
            self.status_celular = False
            print('O celular está desligado!')
        else:
            print('O celular já está desligado!')

    def fazer_chamada(self):
        if self.status_celular:
            if self.status_chamada:
                print('Você já está fazendo uma chamada!')
            else:
                self.status_chamada = True
                print('Você está fazendo uma chamada!')
        else:
            print('O celular está desligado!')

    def encerrar_chamada(self):
        if self.status_celular:
            if self.status_chamada:
                self.status_chamada = False
                print('A chamada foi encerrada!')
            else:
                print('Você não está fazendo nenhuma chamada!')
        else:
            print('O celular está desligado!')

celular1 = Celular(marca="Samsung", modelo="S24", polegadas=7.1, armazenamento=512, mem_ram=16)

Celular.ligar(celular1)

celular1.ligar()
celular1.fazer_chamada()
celular1.encerrar_chamada()
celular1.desligar()
celular1.fazer_chamada()
celular1.encerrar_chamada()
celular1.desligar()
celular1.desligar()

# Atividade 03

