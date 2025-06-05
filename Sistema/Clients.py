"""
Módulo de Clientes
"""
import Utils as u


def clients_list(clients: dict):
    for key, value in clients.items():
        print(key)
        print(value)


def main(menu: tuple, clients: dict):
    """
    Função principal do módulo de clientes

    :param menu: Informar opções do menu
    :param clients: Informaro dicionário de dados dos clientes
    :return: Nada
    """
    while True:
        op = u.show_menu(menu, 1, 6)
        if op == 1:
            pass
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            clients_list(clients)
        elif op == 5:
            pass
        else:
            break

if __name__ == '__main__':
    menu = (
        "1. Cadastrar Clientes",
        "2. Editar Cliente",
        "3. Remover Cliente",
        "4. Listar Clientes",
        "5. Pesquisar Cliente",
        "6. Voltar ao Menu Anterior"
    )
    dict = {
        "00697355900": {
            "nome": "Maicris",
            "idade": 48
        }
    }
    main(menu, dict)