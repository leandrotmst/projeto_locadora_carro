# SISTEMA DE MANUTENÇÃO DOS VEÍCULOS
from carros import dict_carros


def main():
    try:
        carro = input('Digite o carro que precisa de manutenção: ')
        if carro in dict_carros:
            informar_manutencao(carro)
            return carro
        else:
            print('Digite o nome de um carro válido.')
    except ValueError:
        print('Digite algo válido.')


def informar_manutencao(carro):
    problema = input('Informe o problema do carro: ')
    print(f'{carro} precisa de manutenção, está com problema de {problema}.')


