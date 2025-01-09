# Atividade 1

print('######### Programa para somar as notas e calcular a média #########')

listaNotas = []

def solicitarNotas():
    qntd_numeros = int(input('\nQuantas notas deseja digitar? '))

    for contador in range(qntd_numeros):
        while True:
            try:
                nota = input(f'Digite a {contador + 1}º nota ou "s" para sair: ').lower()
                if nota == 's':
                    print('Saindo da entrada de notas...')
                    return

                nota = float(nota.replace(',', '.'))

                if nota < 0 or nota > 10:
                    print('Nota inválida. Por favor, digite uma nota entre 0 e 10.')
                else:
                    listaNotas.append(nota)
                    break
            except ValueError:
                print('Entrada inválida. Por favor, insira um número válido.')

solicitarNotas()

if listaNotas:
    media = sum(listaNotas) / len(listaNotas)
    print(f'\nA média das notas é {media:.2f}')
else:
    print('\nNenhuma nota válida foi inserida.')


# Atividade 2

def calcularAreaRetangulo(base, altura):
    return base * altura

base = int(input('Digite a base do retângulo: '))
altura = int(input('Digite a altura do retângulo: '))

areaRetangulo = calcularAreaRetangulo(base, altura)

print(f'A área do retangulo é {areaRetangulo}')

# Atividade 3

def concatenar_strings(*args):
    if not args:
        print("Nenhuma palavra foi fornecida.")
        return ""

    return ' '.join(args)

qntd_palavras = int(input('Quantas palavras deseja digitar? '))

palavras = []

for contador in range(qntd_palavras):
    palavra = input(f'Digite a {contador + 1}º palavra: ')
    palavras.append(palavra)    

resultado = concatenar_strings(*palavras)

print(f'\nStrings concatenadas: {resultado}')

# Atividade 4

numeros = []

def receber_numeros():

    while True:
        try:
            numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))
            if numero == 0:
                break
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
    
def dobrar(numero):
    return numero * 2

receber_numeros()

dobrar_numeros = list(map(dobrar, numeros))

print("Números dobrados:", dobrar_numeros)

# Atividade 5

numeros = []

def receber_numeros():
    while True:
        try:
            numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))
            if numero == 0:
                break
            numeros.append(numero)
        except ValueError:
            print("Por favor, digite um número inteiro válido.")

def numeros_pares(numero):
    return numero % 2 == 0

receber_numeros()

pares = list(filter(numeros_pares, numeros))

print(f'Os nuúmeros pares são: {pares}')

# Atividade 6

from functools import reduce

palavras = []

def receber_palavras():
    
    qntd_palavras = int(input('Quantas palavras deseja digitar? '))
    
    for contador in range(qntd_palavras):
        palavra = input(f'Digite a {contador + 1}º palavra: ')
        palavras.append(palavra)

def maior_palavra():
    return reduce(lambda x, y: x if len(x) > len(y) else y, palavras)

receber_palavras()
maior_palavra = maior_palavra()
print(f'\nA maior palavra da lista é {maior_palavra}')

# ATividade 7

def criar_lista_de_compras():
    lista_de_compras = []
    print("Digite os itens da lista de compras. Digite 'sair' para encerrar.")
    
    while True:
        item = input("Digite um item: ").strip()
        if not item:
            print("Item inválido. Por favor, digite algo.")
            continue
        if item.lower() == 'sair':
            break
        lista_de_compras.append(item)
    
    return lista_de_compras

def exibir_lista_de_compras(lista):
    print("\n-------------------------")
    print("Lista de Compras:")
    print("-------------------------\n")
    for item in lista:
        print(f"- {item}")
    print("\n-------------------------")

def main():
    lista_de_compras = criar_lista_de_compras()
    exibir_lista_de_compras(lista_de_compras)

main()

# Atividade 8

def calcular(numero1, numero2):
    operacao = input('Digite a operação desejada (+, -, *, /): ')
    
    if operacao == '+':
        return lambda numero1, numero2: int(numero1 + numero2)
    elif operacao == '-':
        return lambda numero1, numero2: int(numero1 - numero2)
    elif operacao == '*':
        return lambda numero1, numero2: int(numero1 * numero2)
    elif operacao == '/':
        if numero2 != 0:
            return lambda numero1, numero2: int(numero1 / numero2)
        else:
            return lambda numero1, numero2: 'Divisão por zero não é permitida.'
    else:
        return lambda numero1, numero2: 'Operação inválida'

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

resultado = calcular(num1, num2)
print(f'Resultado: {resultado(num1, num2)}')

# Desafio Pratico 1

def processador_texto(texto):
    
    def exibir_menu():
        print("""
        -------------------------
        1 - Contar palavras
        2 - Contar letras
        3 - Inverter texto
        4 - Substituir palavra-chave
        0 - Sair
        -------------------------
        """)

    def contar_palavras(texto):
        return len(texto.split())

    def contar_letras(texto):
        return sum(1 for char in texto if char.isalpha())

    def inverter_texto(texto):
        return texto[::-1]

    def substituir_palavra(texto, palavra_antiga, palavra_nova):
        return texto.replace(palavra_antiga, palavra_nova)

    while True:
        exibir_menu()
        opcao = input('Digite a opção desejada: ')

        if opcao == '0':
            print('\n----------------------')
            print('Programa encerrado')
            print('----------------------\n')
            break

        if opcao == '1':
            print(f"Número de palavras: {contar_palavras(texto)}")
        elif opcao == '2':
            print(f"Número de letras: {contar_letras(texto)}")
        elif opcao == '3':
            print(f"Texto invertido: {inverter_texto(texto)}")
        elif opcao == '4':
            palavra_antiga = input("Digite a palavra que deseja substituir: ")
            palavra_nova = input("Digite a nova palavra: ")
            texto = substituir_palavra(texto, palavra_antiga, palavra_nova)
            print(f"Texto atualizado: {texto}")
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

texto = input('Digite o texto: ')
processador_texto(texto)

# Desafio Pratico 2 e 3

def processador_texto(texto, **kwargs):
    operacoes = {
        "contar_palavras": lambda txt: len(txt.split()),
        "contar_letras": lambda txt: sum(1 for char in txt if char.isalpha()),
        "inverter_texto": lambda txt: txt[::-1],
        "substituir_palavra": lambda txt, antiga, nova: txt.replace(antiga, nova),
    }

    resultado = texto

    if "contar_palavras" in kwargs and kwargs["contar_palavras"]:
        print(f"Contagem de palavras: {operacoes['contar_palavras'](resultado)}")

    if "contar_letras" in kwargs and kwargs["contar_letras"]:
        print(f"Contagem de letras: {operacoes['contar_letras'](resultado)}")

    if "inverter_texto" in kwargs and kwargs["inverter_texto"]:
        resultado = operacoes["inverter_texto"](resultado)

    if "substituir_palavra" in kwargs:
        antiga = kwargs.get("substituir_palavra")
        nova = kwargs.get("nova_palavra", "")
        if antiga:
            resultado = operacoes["substituir_palavra"](resultado, antiga, nova)

    return resultado

def exibir_menu():
    print("""
    -------------------------
    1 - Contar palavras
    2 - Contar letras
    3 - Inverter texto
    4 - Substituir palavra-chave
    0 - Sair
    -------------------------
    """)

def main():
    texto = input("Digite o texto inicial: ")
    while True:
        exibir_menu()
        opcao = input('Digite a opção desejada: ')

        if opcao == '0':
            print('\n----------------------')
            print('Programa encerrado')
            print('----------------------\n')
            break

        if opcao == '1':
            print(f"Número de palavras: {len(texto.split())}")
        elif opcao == '2':
            print(f"Número de letras: {sum(1 for char in texto if char.isalpha())}")
        elif opcao == '3':
            print(f"Texto invertido: {texto[::-1]}")
        elif opcao == '4':
            palavra_antiga = input("Digite a palavra que deseja substituir: ")
            palavra_nova = input("Digite a nova palavra: ")
            texto = texto.replace(palavra_antiga, palavra_nova)
            print(f"Texto atualizado: {texto}")
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')

if __name__ == "__main__":
    main()
