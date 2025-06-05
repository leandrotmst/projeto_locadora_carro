# SISTEMA DE CÁLCULO PARA LOCAÇÃO DE CARRO
from carros import *


def main():
    while True:
        try:
            carro_nome = input('Digite o modelo do carro: ')
            if carro_nome in dict_carros:
                ano = int(input('Digite o ano do carro (2024 - 2025): '))
                buscar_preco(carro_nome, ano)
            else:
                print('Digite um nove de carro válido!')
            dias = int(input('Digite o número de dias que o usuário quer alugar o carro: '))
            preco = buscar_preco(carro_nome, ano)
            calcular_preco(dias, preco)
            return carro_nome, ano, preco, dias
        except ValueError:
            print('Você digitou algum valor inválido.')


def buscar_preco(carro_nome, ano):
        preco = dict_carros[carro_nome]
        if ano < 2024 and ano > 2025:
            print('Digite um ano possível.')
        elif ano == 2024:
            preco -= 2
            return preco
        elif ano == 2025:
            preco = preco
            return preco

    

def calcular_preco(dias, preco):
    if preco != None:
        conta = dias * preco
        print('O preço do aluguel do carro para esse tanto de dias é', conta, 'reais')
    else:
        print('Digite um ano possível.')
