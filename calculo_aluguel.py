from carros import dict_carros
import pandas as pd
import os
import utils as u 

RENTAL_EXCEL_FILE = 'alugueis_registrados.xlsx'

def main():
    while True:
        menu_aluguel = (
            "1. Calcular Novo Aluguel",
            "2. Remover Aluguel Registrado",
            "3. Sair do Módulo de Aluguel"
        )
        op = u.show_menu(menu_aluguel, 1, 3) 

        if op == 1:
            try:
                carro_nome = input('Digite o modelo do carro: ')
                if carro_nome in dict_carros:
                    dias = u.get_int_value('Digite o número de dias que o usuário quer alugar o carro: ', 1, 365) 
                    ano = u.get_int_value('Digite o ano do carro (2024 - 2025): ', 2024, 2025)
                    
                    preco_diaria = buscar_preco(carro_nome, ano)
                    if preco_diaria is not None:
                        preco_total = calcular_preco(dias, preco_diaria)
                        
                        if preco_total is not None:
                            try:
                                rental_data = {
                                    'Carro': carro_nome,
                                    'Dias Alugados': dias,
                                    'Ano do Carro': ano,
                                    'Preço Diária': preco_diaria,
                                    'Preço Total': preco_total
                                }
                                
                                if os.path.exists(RENTAL_EXCEL_FILE):
                                    df = pd.read_excel(RENTAL_EXCEL_FILE)
                                    new_rental_df = pd.DataFrame([rental_data])
                                    df = pd.concat([df, new_rental_df], ignore_index=True)
                                else:
                                    df = pd.DataFrame([rental_data])
                                
                                df.to_excel(RENTAL_EXCEL_FILE, index=False)
                                print(f"Aluguel de '{carro_nome}' para {dias} dias registrado com sucesso no Excel.")
                            except Exception as e:
                                print(f"Erro ao adicionar aluguel ao Excel: {e}")
                            
                    
                else:
                    print('Digite um nome de carro válido!')
            except ValueError:
                print('Você digitou algum valor inválido.')
        elif op == 2:
            remover_aluguel()
        elif op == 3:
            print("Saindo do Módulo de Aluguel.")
            break


def buscar_preco(carro_nome, ano):
    preco = dict_carros.get(carro_nome)
    if preco is None:
        print(f"Carro '{carro_nome}' não encontrado no dicionário.")
        return None

    if ano == 2024:
        return preco - 2
    elif ano == 2025:
        return preco
    else:
        print('Digite um ano possível (2024 ou 2025).')
        return None
    

def calcular_preco(dias, preco_diaria):
    if preco_diaria is not None:
        conta = dias * preco_diaria
        print(f'O preço do aluguel do carro para {dias} dias é {conta:.2f} reais')
        return conta
    else:
        print('Há algum problema com as informações que você digitou!')
        return None

def remover_aluguel():
    if not os.path.exists(RENTAL_EXCEL_FILE):
        print("Arquivo de aluguéis Excel não encontrado. Nenhum aluguel para remover.")
        return

    try:
        df = pd.read_excel(RENTAL_EXCEL_FILE)
        if df.empty:
            print("Nenhum aluguel registrado na planilha.")
            return

        print("\n--- Aluguéis Registrados ---")
        print(df.to_string(index=False))
        print("----------------------------")

        carro_para_remover = input("Digite o nome do carro do aluguel a ser removido (exato): ")
        
        initial_rows = len(df)
        df_filtered = df[df['Carro'] != carro_para_remover]

        if len(df_filtered) < initial_rows:
            df_filtered.to_excel(RENTAL_EXCEL_FILE, index=False)
            print(f"Aluguel(is) do carro '{carro_para_remover}' removido(s) do Excel.")
        else:
            print(f"Aluguel do carro '{carro_para_remover}' não encontrado.")
    except Exception as e:
        print(f"Erro ao remover aluguel do Excel: {e}")