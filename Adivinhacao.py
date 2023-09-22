# Adivinha um número inteiro que o usuário esteja pensando.

import random
import os
import time

# Função para solicitar e validar a tentativa.
def TentativaDeAdivinhacao(numero_aleatorio, limite_minimo, limite_maximo):

    retorno = False
    tentativa = int(input("Tente um número entre {} e {}: ".format(limite_minimo,limite_maximo)))

    # Validação para conferir a diferença entre positiva entre os números e definir se está muito perto ou muito longe.
    quente_ou_frio = abs(numero_aleatorio - tentativa)

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

# Mensagens de motivação ao final da partida.
def MensagemFinal(tentativa):
    
    if (tentativa == 1):
        print("Em {} Tentativa! Impossível! - [Thanos]".format(tentativa))
    elif (tentativa <= 3):
        print("Em {} Tentativas! Que satisfação, aspira! - [Coronel Otávio]".format(tentativa))
    elif (tentativa <= 4):
        print("Em {} Tentativas! Elementar, meu caro Watson! - [Scherlock Holmes]".format(tentativa))
    elif (tentativa <= 5):
        print("Em {} Tentativas! Boa Zero Meia! Padrão! - [Capitão Nascimento]'".format(tentativa))
    elif (tentativa <= 6):
        print("Em {} Tentativas! Vamos colocar um sorriso nesse rosto! - [Coringa]".format(tentativa))
    elif (tentativa <= 7):
        print("Em {} Tentativas! Wilsoooooooonnnnnnnn! - [O Náufrago]".format(tentativa))
    elif (tentativa <= 8):
        print("Em {} Tentativas! Não vai subir ninguém! '- [Capitão Nascimento]'".format(tentativa))
    elif (tentativa <= 9):
        print("Em {} Tentativas! A culpa é minha e eu coloco em quem eu quiser! - [Homer Simpson]".format(tentativa))
    elif (tentativa <= 10):
        print("Em {} Tentativas! Houston, we have a problem - [Apollo]".format(tentativa))
    else: 
        print("Em {} Tentativas! Pede pra Sair - [Capitão Nascimento]".format(tentativa))

# Início do jogo.
def main():
    print("************************************")
    print("* Bem vindo ao jogo de Adivinhação *")
    print("************************************")

    # Animação de Aguarde.
    time.sleep(1.5)
    print() 
    
    while True:
        print("------------------------------------")
        print("  Uma nova rodada vai para Começar  ")
        print("------------------------------------")
        print()

        # Configuração da geração dos números aleatórios.
        limite_minimo,limite_maximo = 1, 100
        # Gerando um número aleatório entre 1 e 100.
        numero_aleatorio = int(random.randint(limite_minimo, limite_maximo))  
        tentativa = 0

        while True:
            tentativa=tentativa + 1
            resultado = TentativaDeAdivinhacao(numero_aleatorio, limite_minimo, limite_maximo)
            print()

            if resultado:
                break
        
        MensagemFinal(tentativa)
        print()

        nova_partida = input("Iniciar Nova Partida (S/N)? ").strip().lower()
        os.system('clear')

        if nova_partida != "s":
            print("Fim de Jogo!")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()
