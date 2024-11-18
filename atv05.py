# Atividade 1

print('######### Programa para somar as notas e calcular a média #########')

listaNotas = set()

def solicitarNotas():
    while True:
        nota = input('Digite uma nota ou s para sair: ')
        if nota == 's':
            break
        else:
            listaNotas.add(float(nota))

solicitarNotas()

media = sum(listaNotas) / len(listaNotas)

print(media)

# Atividade 2

def calcularAreaRetangulo(base, altura):
    return base * altura

base = int(input('Digite a base do retângulo: '))
altura = int(input('Digite a altura do retângulo: '))

areaRetangulo = calcularAreaRetangulo(base, altura)

print(f'A área do retangulo é {areaRetangulo}')

# Atividade 3

