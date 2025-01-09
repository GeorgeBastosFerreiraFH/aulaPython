import json
import os

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_arquivo = os.path.join(diretorio_atual, "producao_anual.json")

try:
    with open(caminho_arquivo, "r") as file:
        producao_anual = json.load(file)
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
    exit()

def calcular_producao_total_ano(ano):
    total_producao = 0
    for fazenda in producao_anual["Fazendas"].values():
        for cultura in fazenda.values():
            total_producao += cultura[ano]
    return total_producao

def analisar_anos():
    producao_max = 0
    producao_min = float('inf')
    ano_max = ano_min = 0

    for i, ano in enumerate(producao_anual["Ano"]):
        producao_total_ano = calcular_producao_total_ano(i)
        
        if producao_total_ano > producao_max:
            producao_max = producao_total_ano
            ano_max = ano
        
        if producao_total_ano < producao_min:
            producao_min = producao_total_ano
            ano_min = ano

    print(f"O ano com a maior produção total foi {ano_max} com {producao_max} unidades.")
    print(f"O ano com a menor produção total foi {ano_min} com {producao_min} unidades.")

def analisar_culturas():
    cultura_max = cultura_min = ""
    producao_max_cultura = producao_min_cultura = float('inf')

    culturas_totais = {}
    for fazenda in producao_anual["Fazendas"].values():
        for cultura, producao in fazenda.items():
            if cultura not in culturas_totais:
                culturas_totais[cultura] = [0] * len(producao_anual["Ano"])
            for i, quantidade in enumerate(producao):
                culturas_totais[cultura][i] += quantidade

    for cultura, producao in culturas_totais.items():
        producao_total_cultura = sum(producao)
        if producao_total_cultura > producao_max_cultura:
            producao_max_cultura = producao_total_cultura
            cultura_max = cultura
        
        if producao_total_cultura < producao_min_cultura:
            producao_min_cultura = producao_total_cultura
            cultura_min = cultura

    print(f"A cultura com a maior produção total foi {cultura_max} com {producao_max_cultura} unidades.")
    print(f"A cultura com a menor produção total foi {cultura_min} com {producao_min_cultura} unidades.")

def analisar_fazenda_ano(ano):
    producao_max_fazenda = 0
    producao_min_fazenda = float('inf')
    fazenda_max = fazenda_min = ""

    ano_index = producao_anual["Ano"].index(ano)

    for fazenda, culturas in producao_anual["Fazendas"].items():
        producao_total_fazenda = sum(culturas[cultura][ano_index] for cultura in culturas)

        if producao_total_fazenda > producao_max_fazenda:
            producao_max_fazenda = producao_total_fazenda
            fazenda_max = fazenda
        
        if producao_total_fazenda < producao_min_fazenda:
            producao_min_fazenda = producao_total_fazenda
            fazenda_min = fazenda

    print(f"A fazenda com a maior produção no ano {ano} foi {fazenda_max} com {producao_max_fazenda} unidades.")
    print(f"A fazenda com a menor produção no ano {ano} foi {fazenda_min} com {producao_min_fazenda} unidades.")


analisar_anos()
analisar_culturas()

ano_escolhido = int(input("Digite o ano que deseja analisar 2019-2024: "))
analisar_fazenda_ano(ano_escolhido)
