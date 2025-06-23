import pandas as pd
import os

LUCRO_EXCEL_FILE = 'lucro_mensal.xlsx'

def main():
    try:
        faturamento = float(input('Digite o faturamento mensal da locadora: '))
        imposto = float(input('Digite o valor do custo dos impostos: '))
        aluguel = float(input('Digite o custo do aluguel da locadora: '))
        manutencao = float(input('Digite o custo de manutenção dos carros: '))
        seguros = float(input('Digite o valor dos custos dos seguros: '))
        salarios = float(input('Digite o valor dos custos dos salários dos funcionários: '))
        marketing = float(input('Digite o valor do custo do marketing: '))
        
        if any(val < 0 for val in [faturamento, imposto, aluguel, manutencao, seguros, salarios, marketing]):
            print('Os valores de faturamento, custos e despesas não podem ser negativos.')
            return
            
        conta_custos, despesas = calcular_lucro(faturamento, imposto, aluguel, manutencao, seguros, salarios, marketing)
        
        print(f'Seu lucro vai ser {conta_custos:.2f} reais') 
        
        try:
            lucro_data = {
                'Faturamento': faturamento,
                'Imposto': imposto,
                'Aluguel_Custo': aluguel,
                'Manutencao': manutencao,
                'Seguros': seguros,
                'Salarios': salarios,
                'Marketing': marketing,
                'Total_Despesas': despesas,
                'Lucro_Mensal': conta_custos
            }
            
            if os.path.exists(LUCRO_EXCEL_FILE):
                df = pd.read_excel(LUCRO_EXCEL_FILE)
                new_lucro_df = pd.DataFrame([lucro_data])
                df = pd.concat([df, new_lucro_df], ignore_index=True)
            else:
                df = pd.DataFrame([lucro_data])
            
            df.to_excel(LUCRO_EXCEL_FILE, index=False)
            print(f"Lucro mensal registrado no Excel.")
        except Exception as e:
            print(f"Erro ao adicionar lucro ao Excel: {e}")
        
        return faturamento, imposto, aluguel, manutencao, seguros, salarios, marketing
    except ValueError:
        print('Digite valores válidos (use o "." ao invés da ",") para os custos e faturamento.')

def calcular_lucro(faturamento, imposto, aluguel, manutencao, seguros, salarios, marketing):
    despesas = imposto + aluguel + manutencao + seguros + salarios + marketing
    conta_custos = faturamento - despesas
    return conta_custos, despesas