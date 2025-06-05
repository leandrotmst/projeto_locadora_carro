# SISTEMA DE REGISTRO DE LOCALAÇÃO DE CARRO
from carros import dict_carros
import utils as u
import main as mn

users = {}

def register(menu:tuple):
    while True:
        op = u.show_menu(menu, 1, 3)
        if op == 1:
            nome = input('Digite o nome a ser registrado: ')
            email = input('Digite o e-mail do usuário: ')
            if nome.isalpha() and '@' in email and '.' in email:
                register_user(nome, email)
            else:
                print('Informe um nome ou e-mail válido.')
        elif op == 2:
            remover_user(input('Digite o nome a ser removido: '))
        elif op == 3:
            exibir()
        elif op == 4:
            mn.main(mn.menu)
        else:
            print('Obrigado e volte sempre!!')
            break

def register_user(nome, email):
    users[nome] = email


def remover_user(nome):
    if nome in users:
        del users[nome]
        print('Usuário removido')
    else:
        print('Digite um nome válido.')


def exibir():
    for key, values in users.items():
        print()
        print(f'{key}: {values}')



if __name__ == '__main__':
    menu = (
        '1. Registrar usuário',
        '2. Remover usuário',
        '3. Exibir usuário',
    )   
    register(menu)