# Adivinha um número inteiro que o usuário esteja pensando.

import random
import time

print("************************************")
print("* Bem vindo ao jogo de Adivinhação *")
print("************************************")

# Configuração da geração dos números aleatórios.
limite_minimo = 1
limite_maximo = 100

numero_aleatorio = int(random.randint(limite_minimo, limite_maximo))  # Gerando um número aleatório entre 1 e 100.
print()

# Função para solicitar e validar a tentativa.
def TentativaDeAdivinhacao(numero_aleatorio, limite_minimo, limite_maximo):

    retorno = False
    tentativa = int(input("Tente um número entre {} e {}: ".format(limite_minimo,limite_maximo)))

    # Validação para conferir a diferença entre positiva entre os números e definir se está muito perto ou muito longe.
    quente_ou_frio = (numero_aleatorio - tentativa)
    if (quente_ou_frio < 0):
        quente_ou_frio = -quente_ou_frio

    # Valida se ocorreu a vitória.
    if (tentativa == numero_aleatorio):
        print("Você acretou!")
        retorno =  True
    
    # Valida se o valor informado está entre o Range de geração do número aleatório.
    elif (limite_minimo < tentativa > limite_maximo):
        print("Você digitou um numero inválido.")

    # Ofereve dicas para se aproximar do valor correto.
    else:
        if quente_ou_frio < 10:
            if numero_aleatorio > tentativa:
                print("Dica: Um pouco mais! Está ficando quente ...")
            else:
                print("Dica: Um pouco menos! Está ficando quente ...")
        else:
            if numero_aleatorio > tentativa:
                print("Dica: Um pouco mais! Está muito frio ...")
            else:
                print("Dica: Um pouco menos! Está muito frio ...")

    # Fim da função
    return retorno

# Início do jogo.
while True:

    resultado = TentativaDeAdivinhacao(numero_aleatorio, limite_minimo, limite_maximo)
    print()

    if (resultado == True):
        time.sleep(5)
        break
