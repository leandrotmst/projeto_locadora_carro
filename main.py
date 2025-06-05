import utils as u
import registrar_user as ru
import manutencao as m
import calculo_aluguel as ca
import lucro


def main(menu: tuple):
	menu_register = (
        '1. Registrar usuário',
        '2. Remover usuário',
        '3. Exibir usuário',
    )   
	while True:
		op = u.show_menu(menu, 1, 4)
		if op == 1:
			ru.register(menu_register)
		elif op == 2:
			ca.main()
		elif op == 3:
			m.main()
		elif op == 4:
			lucro.main()
		elif op == 5:
			print('Obrigado, volte sempre!!')
			break
		else:
			print('Faça uma escolha dentre as opções.')

if __name__ == '__main__':
	menu = (
		"1. Módulo de Clientes",
		"2. Cálculo de Aluguel de Carro",
		"3. Registrar Manutenção de Veículo",
		"4. Cálculo de Lucro Mensal",
		"5. Sair do Sistema",
	)
	main(menu)