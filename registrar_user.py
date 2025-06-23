# SISTEMA DE REGISTRO DE LOCALAÇÃO DE CARRO
import utils as u
import pandas as pd
import os

users = {}
USER_EXCEL_FILE = 'usuarios_registrados.xlsx'

menu_register = (
    '1. Registrar usuário',
    '2. Remover usuário',
    '3. Exibir usuário',
    '4. Voltar ao menu principal', 
    '5. Sair' 
)

def load_users_from_excel():
    global users
    if os.path.exists(USER_EXCEL_FILE):
        try:
            df = pd.read_excel(USER_EXCEL_FILE)
            if 'Nome' in df.columns and 'Email' in df.columns:
                users = df.set_index('Nome')['Email'].to_dict()
                print("Usuários carregados do Excel.")
            else:
                print("Arquivo Excel de usuários não contém as colunas esperadas (Nome, Email).")
                users = {} 
        except Exception as e:
            print(f"Erro ao carregar usuários do Excel: {e}")
    else:
        print("Arquivo Excel de usuários não encontrado. Iniciando com usuários vazios.")

load_users_from_excel()

def register(menu:tuple):
    while True:
        op = u.show_menu(menu, 1, 5)
        if op == 1:
            nome = input('Digite o nome a ser registrado: ')
            email = input('Digite o e-mail do usuário: ')
            if '@' in email and '.' in email:
                register_user(nome, email)
                print(f"Usuário {nome} registrado com sucesso!")
            else:
                print()
                print('INFORME UM E-MAIL VÁLIDO!')
                print()
        elif op == 2:
            remover_user(input('Digite o nome a ser removido: '))
        elif op == 3:
            exibir()
        elif op == 4: 
            break
        elif op == 5: 
            print('Obrigado, volte sempre!!')
            import sys
            sys.exit()


def register_user(nome, email):
    if nome in users:
        print(f"Usuário '{nome}' já existe. Atualizando e-mail para '{email}'.")
        users[nome] = email 
    else:
        users[nome] = email
    
    try:
        if os.path.exists(USER_EXCEL_FILE):
            df = pd.read_excel(USER_EXCEL_FILE)
            df = df[df['Nome'] != nome]
            
            new_user_df = pd.DataFrame([{'Nome': nome, 'Email': email}])
            df = pd.concat([df, new_user_df], ignore_index=True)
        else:
            df = pd.DataFrame([{'Nome': nome, 'Email': email}])
        
        df.to_excel(USER_EXCEL_FILE, index=False)
        print(f"Usuário '{nome}' adicionado/atualizado no Excel.")
    except Exception as e:
        print(f"Erro ao adicionar/atualizar usuário ao Excel: {e}")


def remover_user(nome):
    global users
    if nome in users:
        del users[nome]
        print(f'Usuário "{nome}" removido da memória.')
        
        try:
            if os.path.exists(USER_EXCEL_FILE):
                df = pd.read_excel(USER_EXCEL_FILE)
                df = df[df['Nome'] != nome]
                df.to_excel(USER_EXCEL_FILE, index=False)
                print(f'Usuário "{nome}" removido do Excel.')
            else:
                print('Arquivo Excel de usuários não encontrado para remoção.')
        except Exception as e:
            print(f"Erro ao remover usuário do Excel: {e}")
    else:
        print('Usuário não encontrado.')


def exibir():
    print("\n--- Usuários Registrados (do Excel) ---")
    if os.path.exists(USER_EXCEL_FILE):
        try:
            df = pd.read_excel(USER_EXCEL_FILE)
            if not df.empty:
                print(df.to_string(index=False))
            else:
                print("Nenhum usuário registrado no Excel.")
        except Exception as e:
            print(f"Erro ao ler usuários do Excel para exibição: {e}")
    else:
        print("Arquivo Excel de usuários não encontrado.")
    print("---------------------------------------")


if __name__ == '__main__':
    register(menu_register)