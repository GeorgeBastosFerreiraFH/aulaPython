# Missão 3: O enigma do guardião

soma = 0

for numero in range(101):
    if numero % 2 == 0:
        soma += numero

print(f'Passagem permitida, a soma de todos os números pares são {soma}.') 

# Missão 4: Resgate da Princesa na Torre (incompleto)

def dobrarNumeros(lista):
    return list(map(lambda x: x * 2, lista))

portas = set()

for numeroPorta in range (1, 8):
    numeroDigitado = input(f'Acerte o numero correto para abrir a porta {numeroPorta}: ')
    portas.add(int(numeroPorta))
    resultado = dobrarNumeros(portas)
    print(resultado)

    if numeroDigitado == resultado:
        print('Você acertou')
    elif numeroDigitado != resultado:
        print('Você errou tente novamente')
    else:
        print('Você digitou algo errado')





