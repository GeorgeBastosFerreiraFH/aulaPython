print('------------------------------------')
# Atividade 1

listaDeNumeros = [1, 2, 3, 4, 5]

print('Elementos da lista de números: ')
for i in listaDeNumeros:
  print(i)

print('------------------------------------')
# Atividade 2

listaDeLetras = ['a', 'e', 'i', 'o', 'u']

print('Elementos da lista de letras: ')
for i in listaDeLetras:
  print(i)

print('------------------------------------')
# Atividade 3

listaMista = ['Gabriel', 9, '3º Elemento', True, 8.9]

print(f"Esse é o terceiro elemento da lista mista: {listaMista[2]}")

print('------------------------------------')
# Atividade 4

palestrantes = (
    ("Ana Silva", "Inteligência Artificial", "Universidade Federal de São Paulo"),
    ("Bruno Almeida", "Desenvolvimento Web", "Instituto de Tecnologia de São Paulo"),
    ("Carla Souza", "Cibersegurança", "Universidade Estadual de Campinas")
)

nome, tema, instituicao = palestrantes[2]

print(f"Nome: {nome}, Tema: {tema}, Instituição: {instituicao}")

print('------------------------------------')
# Desafio Prático

resultados = [
    ("Equipe A", [15, 20, 18, 25, 22]),
    ("Equipe B", [10, 17, 23, 19, 21]),
    ("Equipe C", [20, 18, 20, 23, 24]),
    ("Equipe D", [25, 30, 28, 26, 29]),
    ("Equipe E", [12, 14, 13, 15, 17]),
    ("Equipe F", [19, 21, 22, 20, 18]),
    ("Equipe G", [22, 24, 26, 23, 25]),
    ("Equipe H", [18, 16, 19, 21, 20])
]

medias = [(equipe, sum(pontos) / len(pontos)) for equipe, pontos in resultados]

print("Médias de Pontos por Equipe em ordem decrescente:")
for equipe, media in medias:
    medias.sort(key=lambda elemento: elemento[1], reverse=True)
    print(f"Equipe: {equipe}, Média de Pontos: {media:.2f}")

            # FIM #
print('------------------------------------')