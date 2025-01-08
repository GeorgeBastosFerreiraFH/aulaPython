# Atividade 1

def saudacao():
    nome = input('Qual seu nome: ')
    print(f'Olá {nome}, seja bem vindo!')
    
saudacao()

# Atividade 2

from datetime import datetime

def saudacaoHorario():
    hora = datetime.now().hour
    minutos = datetime.now().minute
    
    if hora >= 6 and hora < 12:
        print(f'Bom dia, são {hora}:{minutos}!')
    elif hora >= 12 and hora < 18:
        print(f'Boa tarde, são {hora}:{minutos}!')
    elif hora >= 18 and hora < 24:
        print(f'Boa noite, são {hora}:{minutos}!')
    # print(f'{hora}:{minutos}')
saudacaoHorario()

# Atividade 3

def somar_numeros():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f'A soma dos números é {num1 + num2}')

somar_numeros()

# Atividade 4

def subtrair_numeros():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f'A subtração dos números é {num1 - num2}')
    
subtrair_numeros()

# Atividade 5

def multiplicar_numeros():
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    print(f'A multiplicação dos números é {num1 * num2}')

multiplicar_numeros()

# Desafio Prático

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def divisão(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"

def exibir_menu():
    print("""
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Divisão
    0 - Sair
    """)

def main():
    
    while True:
        
        exibir_menu()
        opcao = input('Digite a opção desejada: ')
        
        if opcao == '0':
            print('\n----------------------')
            print('Calculadora encerrada')
            print('----------------------\n')
            break
        
        if opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, insira números válidos.")
                continue

            if opcao == '1':
                print(f"Resultado: {somar(num1, num2)}")
            elif opcao == '2':
                print(f"Resultado: {subtrair(num1, num2)}")
            elif opcao == '3':
                print(f"Resultado: {multiplicar(num1, num2)}")
            elif opcao == '4':
                print(f"Resultado: {divisão(num1, num2)}")

        else:
            print('Opção inválida.')

main()
