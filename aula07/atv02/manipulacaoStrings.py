def inverterString(string):
  return f'\nEssa é a palavra invertida {string[::-1]}'

def numeroLetras(string):
  palavra = string.replace(" ", "")
  return f'\nA palavra possue {len(palavra)} letras'

def palavraPalidromo(string):
  string = string.replace(" ", "")
  if string == string[::-1]:
    print(f'\nA palavra {string} é um Palíndromo!')
  else:
    print(f'\nA palavra {string} não é um Palíndromo!')
