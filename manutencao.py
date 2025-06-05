# SISTEMA DE MANUTENÇÃO DOS VEÍCULOS
from carros import dict_carros
import utils as u

def main():
    try:
        carro = input('Digite o carro que precisa de manutenção: ')
        informar_manutencao(carro)
        return carro
    except ValueError:
        print('Digite algo válido.')

def informar_manutencao(carro):
    if carro in dict_carros:
        problema = input('Informe o problema do carro: ')
        print(f'{carro} precisa de manutenção, está com problema de {problema}.')    
    else:
        return ('Informe algum carro possível.')

