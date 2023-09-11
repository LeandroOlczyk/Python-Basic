# Formulas Financeiras de Matemática Financeira

# Calcular o Valor Futuro de Resgate de uma Aplicação
def CalcularValorFuturo():

    valorPresente=float(input('Valor Presente: '))
    taxa=float(input("Taxa Mensal: "))
    periodo=float(input('Meses: '))

    # Converter o valor informado pelo usuário para Percentual.
    taxa=(taxa/100) 

    # VF = VP * (1 + i) ^ N
    valorFuturo=(valorPresente*pow((1+taxa),periodo))

    # Aplicar arredondamento.
    valorFuturo=round(valorFuturo,2)
    
    print('Valor Futuro: ',valorFuturo)
    return 0

# Calular Valor Presente de uma Aplicação Financeira
def CalcularValorPresente():

    valorFuturo=float(input('Valor Futuro: '))
    taxa=float(input("Taxa Mensal: "))
    periodo=float(input('Meses: '))

    # Converter o valor informado pelo usuário para Percentual.
    taxa=(taxa/100) 

    # PV = FV / (1 + i) ^ N
    valorPresente=(valorFuturo/pow(1+taxa,periodo))

    # Aplicar arredondamento.
    valorPresente=round(valorPresente,2)

    print('Valor Presente: ',valorPresente)
    return 0

# Calcular a Taxa necessária para atingir o Valor Futuro desejado.
def CalcularTaxaAplicacao():

    valorPresente=float(input('Valor Presente: '))
    valorFuturo=float(input('Valor Futuro: '))
    periodo=float(input('Meses: '))

    # i = (FV / PV) ^ (1 / N) - 1
    percentualGanhos=(valorFuturo/valorPresente)
    taxa=pow(percentualGanhos,1/periodo)-1

    # Converter a vizualização da Taxa.
    taxa=(taxa*100)
    taxa=round(taxa,4)

    print('Taxa: ',taxa,' %')
    return 0

def switch(case):
    switcher = {
        1: CalcularValorFuturo,
        2: CalcularValorPresente,
        3: CalcularTaxaAplicacao,
    }
    
    # Obter a função correspondente
    funcao = switcher.get(case, lambda: "Opção inválida. Por favor, escolha uma opção válida.")
    return funcao()

# Inicio da Execução
while True:

    print('Selecione a Opção de Calculo desejada:')
    print()
    print('1 - Calcular Valor Futuro.')
    print('2 - Calcular Valor Presente.')
    print('3 - Calcular Taxa de Rendimento.')
    print()
    opcao = int(input("Opção: "))

    switch(opcao)

    print()
    reiniciar = input("Realizar novo calculo (S/N)? ").strip().lower()
    if reiniciar != "s":
        break