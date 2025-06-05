# SISTEMA DE REGISTRO DE LOCALAÇÃO DE CARRO
import utils as u

users = {}

def register(menu:tuple):
    while True:
        op = u.show_menu(menu, 1, 5)
        if op == 1:
            nome = input('Digite o nome a ser registrado: ')
            email = input('Digite o e-mail do usuário: ')
            if nome.isalpha() and '@' in email and '.' in email:
                register_user(nome, email)
                print(f"Usuário {nome} registrado com sucesso!")
            else:
                print('Informe um nome ou e-mail válido.')
        elif op == 2:
            remover_user(input('Digite o nome a ser removido: '))
        elif op == 3:
            exibir()
        elif op == 4:
            break
        elif op == 5:
            print('Obrigado, volte sempre!!')
            return 'EXIT_SYSTEM'
        else:
            print('Selecione uma opção possível.')


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
        '4. Sair deste módulo',
        "5. Sair do Sistema",
    )   
    register(menu)