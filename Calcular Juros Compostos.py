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
    
    msg='Valor Futuro: ',valorFuturo
    return msg

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

    msg='Valor Presente: ',valorPresente
    return msg

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

    msg='Taxa: ',taxa,' %'
    return msg

def switch(case):
    switcher = {
        1: CalcularValorFuturo,
        2: CalcularValorPresente,
        3: CalcularTaxaAplicacao,
    }
    
    # Obter a função correspondente ao caso
    funcao = switcher.get(case, lambda: "Opção inválida. Por favor, escolha uma opção válida.")
    
    # Executar a função e retornar o resultado
    return funcao()

# Exemplo de uso
opcao = int(input("Digite o número da opção desejada: "))
resultado = switch(opcao)
print(resultado)
