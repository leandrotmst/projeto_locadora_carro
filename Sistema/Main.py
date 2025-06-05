"""
Sistema de Vendas
v0.1
05/06/25
by: Maicris Fernandes
"""
import Utils as u
import Clients as c


def main(menu: tuple, dict: dict):
    clients_menu = (
        "1. Cadastrar Clientes",
        "2. Editar Cliente",
        "3. Remover Cliente",
        "4. Listar Clientes",
        "5. Pesquisar Cliente",
        "6. Voltar ao Menu Anterior"
    )
    while True:
        op = u.show_menu(menu, 1, 4)
        if op == 1:
            c.main(clients_menu, dict["clients"])
        elif op == 2:
            pass
        elif op == 3:
            pass
        else:
            print("Obrigado e volte sempre!!!")
            break


if __name__ == '__main__':
    menu = (
        "1. Módulo de Clientes",
        "2. Módulo de Produtos",
        "3. Módulo de Vendas",
        "4. Sair"
    )
    dict = {
        "clients": {},
        "products": {},
        "salles": {}
    }
    main(menu, dict)