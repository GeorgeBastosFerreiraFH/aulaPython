# Funções para Medidas de Comprimento
def metros_para_pes(metros):
    return metros * 3.28084

def pes_para_metros(pes):
    return pes / 3.28084

def quilometros_para_milhas(quilometros):
    return quilometros * 0.621371

def milhas_para_quilometros(milhas):
    return milhas / 0.621371

# Funções para Medidas de Massa
def quilogramas_para_libras(quilogramas):
    return quilogramas * 2.20462

def libras_para_quilogramas(libras):
    return libras / 2.20462

def gramas_para_oncas(gramas):
    return gramas * 0.035274

def oncas_para_gramas(oncas):
    return oncas / 0.035274

# Funções para Temperatura
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15
