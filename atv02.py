print('------------------------------------')
# Atividade 1 e 2

frutas = set()

frutas.add('maçã')
frutas.add('banana')
frutas.add('uva')
frutas.add('laranja')
frutas.add('morango')

print(f'A lista tem essas {frutas} frutas')

frutaEscolhida = input('Escolha uma fruta: ')
frutaEscolhida = frutaEscolhida.lower()

if frutaEscolhida in frutas:
    print(f'A fruta {frutaEscolhida} está na lista')
else:
    print(f'A fruta {frutaEscolhida} não está na lista')

print('------------------------------------')
# Atividade 3 e 4

frutas_vermelhas = set()

frutas_vermelhas.add('morango')
frutas_vermelhas.add('cereja')
frutas_vermelhas.add('framboesa')

print(frutas_vermelhas)

frutas_vermelhas.remove('cereja')
print(frutas_vermelhas)

print('------------------------------------')
# Atividade 5

conjunto_A = {'A', 'C', 'E', 'G', 'I'}
conjunto_B = {'B', 'D', 'F', 'H', 'J'}

print(conjunto_A.union(conjunto_B))

print('------------------------------------')
# Atividade 6

conjunto_um = {1, 2, 3, 4, 5}
conjunto_dois = {4, 5, 6, 7, 8}

print(conjunto_um.intersection(conjunto_dois))

print('------------------------------------')
# Atividade 7

lista1 = input("Digite os elementos da primeira lista, separados por vírgula: ").split(',')
lista2 = input("Digite os elementos da segunda lista, separados por vírgula: ").split(',')

lista1 = [elemento.strip() for elemento in lista1]
lista2 = [elemento.strip() for elemento in lista2]

uniaoListas = list(set(lista1) | set(lista2))

print(f"A união dos elementos únicos das listas é: {uniaoListas}")

print('------------------------------------')
# Atividade 8

pessoas = {
    "Alice" : 30,
    "Bruno" : 25,
    "Carla" : 28,
    "Daniel" : 22,
    "Eva" : 35
}

for nome, idade in pessoas.items():
    print(f"Nome: {nome}, Idade: {idade}")

print('------------------------------------')
# Atividade 9

dicionario_pessoas = dict()

dicionario_pessoas['Gabriel'] = {
    'Idade': 35,
    'Profissão': 'Desenvolvedor',
    'Hobby': 'Jogar'
}

dicionario_pessoas['Ana'] = {
    'Idade': 28,
    'Profissão': 'Designer',
    'Hobby': 'Pintar'
}

dicionario_pessoas['Carlos'] = {
    'Idade': 40,
    'Profissão': 'Professor',
    'Hobby': 'Ler'
}

dicionario_pessoas['Mariana'] = {
    'Idade': 30,
    'Profissão': 'Médica',
    'Hobby': 'Correr'
}

dicionario_pessoas['José'] = {
    'Idade': 25,
    'Profissão': 'Estudante',
    'Hobby': 'Tocar Violão'
}

for nome, dados in dicionario_pessoas.items():
    print(f"Nome: {nome}")
    print(f"Idade: {dados['Idade']}")
    print(f"Profissão: {dados['Profissão']}")
    print(f"Hobby: {dados['Hobby']}")
    print('------------------------------------')

print('------------------------------------')
# Atividade 10 e 11

dicionario = dict()

while True:
    nome = input('Digite um nome: ')
    idade = input('Digite uma idade: ')

    dicionario[nome] = idade

    continuar = input('Deseja continuar? (s/n): ')
    if continuar.lower() == 's':
        continue
    elif continuar.lower() == 'n':
        break
    else:
        print('Opção inválida. Digite "s" para continuar ou "n" para sair.')

for nome, idade in dicionario.items():
    print(f"Nome: {nome}, Idade: {idade}")

print('------------------------------------')


nome = input('Digite um nome para buscar: ')

if nome not in dicionario:
    print('Nome não encontrado')
    print('False')
else:
    print(f'O nome {nome} foi econtrado na lista')
    print('True')

print('------------------------------------')
# Atividade 12

candidatos = {
    'Lula': {'numero_votos': 0},
    'Bolsonaro': {'numero_votos': 0},
    'Ciro': {'numero_votos': 0},
    'Simone': {'numero_votos': 0},
    'Eneas': {'numero_votos': 0}
}

numeros_candidatos = {
    '13': 'Lula',
    '22': 'Bolsonaro',
    '56': 'Eneas',
    '12': 'Ciro',
    '15': 'Simone'
}

print('Os candidatos são:')
for numero, nome in numeros_candidatos.items():
    print(f'- {nome} (Número: {numero})')

while True:
    voto = input('Digite o número do candidato para votar ou 0 para sair: ').strip()
    
    if voto in numeros_candidatos:
        nome_original = numeros_candidatos[voto]
        candidatos[nome_original]['numero_votos'] += 1
        print(f'Voto contabilizado para {nome_original}. Total de votos: {candidatos[nome_original]["numero_votos"]}')
    elif voto == '0':
        break
    else:
        print('Número do candidato não encontrado')

for nome, dados in candidatos.items():
    print(f"Candidato {nome} contabilizou {dados['numero_votos']} votos")

print('------------------------------------')
# Atividade 13

alunos = {
   'Ana': {'notas' : [8.5, 7.0, 9.0, 6.5, 8.0]},
   'Gilberto': {'notas' : [7.0, 8.0, 7.5, 9.0, 6.5]},
   'Carlos': {'notas' : [9.0, 8.5, 7.5, 8.0, 9.5]},
   'Daniela': {'notas' : [6.5, 7.0, 6.0, 6.0, 7.5]},
   'Eduardo': {'notas' : [8.0, 9.0, 7.0, 8.5, 9.0]}
}

for nome, dados in alunos.items():
    media = sum(dados['notas']) / len(dados['notas'])
    print(f"Aluno(a) {nome} ficou com a média: {media:.2f}")

print('------------------------------------')
# Atividade 14

lista_original = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print('Os números da lista original são:')
for numeros in lista_original:
    print(numeros)
    
numero = input("Digite números de 1 a 10 para remover da lista, separados por vírgula (ou 'sair' para encerrar): ")
    
numeros_para_remover = set(int(num.strip()) for num in numero.split(',') if num.strip().isdigit())
    
lista_sem_duplicados = {numero for numero in lista_original if numero not in numeros_para_remover}

print('Os números após remoção são:')
for numeros in lista_sem_duplicados:
    print(numeros)

print('------------------------------------')
# Atividade 15

conjunto1 = set([1, 2, 3, 4, 5])
conjunto2 = set([4, 5, 6, 7, 8])
conjunto3 = set([8, 9, 10, 11, 12])
conjunto4 = set([12, 13, 14, 15, 16])

print(conjunto1 | conjunto2 | conjunto3 | conjunto4)

print('------------------------------------')

# Desafio Prático 1 e 2
# Cadastro de Alunos

alunos = dict()

print('Bem-vindo ao cadastro de alunos')

while True:
    
    nomeAluno = input('Digite o nome do aluno(a): ')
    idadeAluno = int(input('Digite a idade do aluno(a): '))
    
    while True:
        try:
            notaMat = float(input('Digite a nota de Matemática do aluno(a): '))
            if 0 <= notaMat <= 10:
                break
            else:
                print('Nota inválida. A nota tem que estar entre 0 - 10.')
        except ValueError:
            print('Nota inválida. A nota tem que estar entre 0 - 10.')
     
    while True:
        try:
            notaCiencia = float(input('Digite a nota de Ciências do aluno(a): '))
            if 0 <= notaCiencia <= 10:
                break
            else:
                print('Nota inválida. A nota tem que estar entre 0 - 10.')
        except ValueError:
            print('Nota inválida. A nota tem que estar entre 0 - 10.')
     
    while True:
        try:
            notaHist = float(input('Digite a nota de História do aluno(a): '))
            if 0 <= notaHist <= 10:
                break
            else:
                print('Nota inválida. A nota tem que estar entre 0 - 10.')
        except ValueError:
            print('Nota inválida. A nota tem que estar entre 0 - 10.')
    
    alunos[nomeAluno] = {
    'Nome': nomeAluno,
    'Idade': idadeAluno,
    'Notas': (notaMat, notaCiencia, notaHist),
    'Media': (notaMat + notaCiencia + notaHist) / 3
    }
       
    print(f'\nAluno {nomeAluno} cadastrado com sucesso!')

    continuar = input('\nDeseja continuar? (s/n): ')
    if continuar.lower() == 's':
        continue
    elif continuar.lower() == 'n':
        break
    elif continuar.lower() != 's' and continuar.lower() !='n':
        print('Opção inválida. Digite "s" para continuar ou "n" para sair.')
    else:
        print('Opção inválida. Digite "s" para continuar ou "n" para sair.')
    
# media = alunos[nomeAluno]['Media']
# print(media)

print('\nAlunos cadastrados: ')
for contador,(nome, dados) in enumerate(alunos.items(), start=1):
    print(f'\n{contador}º aluno(a)')
    print(f"Nome: {dados['Nome']}")
    print(f"Idade: {dados['Idade']}")
    print(f"Nota Matemática: {dados['Notas'][0]}")
    print(f"Nota Ciências: {dados['Notas'][1]}")
    print(f"Nota História: {dados['Notas'][2]}")
    print('------------------------------------')
    print(f'Média: {dados['Media']:.2f}')
    print('------------------------------------')

melhorMedia = 0

for nome, dados in alunos.items():
    if dados['Media'] > melhorMedia:
        melhorMedia = dados['Media']
        melhorAluno = nome

print('\n#######################################################################')
print(f'Parabéns! O(a) aluno(a) {melhorAluno} tem a melhor média da turma! Média: {melhorMedia:.2f}')
print('#######################################################################')
