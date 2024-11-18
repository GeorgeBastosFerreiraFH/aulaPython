from functools import reduce

def quadrado(numero):
    resultado = numero ** 2
    return resultado

resultado = quadrado(5)

print('O quadrado de 5 é:', resultado)

def mostrar_informacoes(**kwargs):
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

mostrar_informacoes(nome = 'Alice', idade = 30, cidade = 'Exemplo')
mostrar_informacoes(curso = 'Python', nivel = 'Iniciante', plataforma = 'Online')

def minha_funcao(*args, **kwargs):
    for arg in args:
        print(arg)
    for chave, valor in kwargs.items():
        print(f'{chave}: {valor}')

minha_funcao('curriculo', 'desenvolvedor', 'fortaleza', nome = 'alice', sobrenome = 'campos', idade = 25)

quadrado = lambda x: x ** 2
print(quadrado(5))

par = lambda numeroPar: numeroPar % 2 == 0
print(par(10))

name_upperCase = lambda nome: nome.upper()
print(name_upperCase('george'))

par_impar = lambda x: 'par' if x % 2 == 0 else 'ímpar'

print(par_impar(5))
print(par_impar(-2))

validar_usuario = lambda user: 'Erro: Usuário precisa ser definido' if user == '' else ('Usuário não pode ter menos de 4 digitos' if len(user) < 4 else 'Usuário cadastrado com sucesso!')

usuario = input('Digite um usuario: ')
print(validar_usuario(usuario))

numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)

numeros = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, numeros)
print(soma)



