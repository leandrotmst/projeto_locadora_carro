"""
Funções usadas ao longo de todo o sistema
"""

def get_int_value(msg, min, max):
    while True:
        try:
            op = int(input(msg))
            if op >= min and op <= max:
                return op
            else:
                print("Valor fora do range especificado!!!")
        except:
            print("Valor inválido!!!")


def show_menu(menu: tuple, min, max):
    for option in menu:
        print(option)
    return get_int_value("opção >> ", min, max)


if __name__ == '__main__':
    op = get_int_value("Digite algo entre 1 e 5",1, 5)