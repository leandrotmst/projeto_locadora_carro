def main():
    try:
        faturamento = float(input('Digite o faturamento mensal da locadora: '))
        imposto = float(input('Digite o valor do custo dos impostos: '))
        aluguel = float(input('Digite o custo do aluguel da locadora: '))
        manutencao = float(input('Digite o custo de manutenção dos carros: '))
        seguros = float(input('Digite o valor dos custos dos seguros: '))
        salarios = float(input('Digite o valor dos custos dos salários dos funcionários: '))
        marketing = float(input('Digite o valor do custo do marketing: '))
        custos(faturamento, imposto, aluguel, manutencao, seguros, salarios, marketing)
        return faturamento, imposto, aluguel, manutencao, seguros, salarios, marketing
    except ValueError:
        print('Digite valores válidos (use o "." ao invés da ",")')

def custos(faturamento, imposto, aluguel, manutencao, seguros, salarios, marketing):
    despesas = imposto + aluguel + manutencao + seguros + salarios + marketing
    conta_custos = faturamento - despesas
    print('Seu lucro vai ser', conta_custos)

