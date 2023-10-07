import os
import random
import time

# Função que define as variáveis principais do jogo, retornando "Palavra Secreta", "Dica" e "Tamanho" da palavra.
def sorteio_palavra_secreta():  
    
    quantidade_listas = 5
    numero_aleatorio = int(random.randint(0, quantidade_listas-1))

    # Lista de palavras que serão sorteadas utilizando a função "random.choice"
    lista_profissoes = ['MOTORISTA','BOMBEIRO','MUSICO','ENFERMEIRO','CANTOR','CONTADOR','MEDICO','ENGENHEIRO','POLICIAL','PROGRAMADOR']
    lista_frutas = ['ABACATE','LARANJA','TANGERINA','MANGA','CEREJA','ABACAXI','KIWI','JABUTICABA']
    lista_tecnologia = ['COMPUTADOR','TECLADO','CELULAR','IMPRESSORA','CAMERA','INTERNET']
    lista_limpeza = ['RODO','AMACIANTE','BALDE','ESPONJA','PANO','VASSOURA']
    lista_animais = ['CACHORRO','GATO','COBRA','GORILA','CAVALO','PAPAGAIO','CORUJA','SAPO','PELICANO']

    # Iniciando a variável.
    dica = "Sem dica"

    # Definindo o retorno aleatório conforme a lista.
    # Palavra secreta sempre será convertida em caixa alta.
    if numero_aleatorio == 0:
        palavra_secreta = random.choice(lista_profissoes).upper()
        dica = "Profissão"
    elif numero_aleatorio == 1:
        palavra_secreta = random.choice(lista_frutas).upper()
        dica = "Fruta"
    elif numero_aleatorio == 2:
        palavra_secreta = random.choice(lista_tecnologia).upper()
        dica = "Tecnologia"
    elif numero_aleatorio == 3:
        palavra_secreta = random.choice(lista_limpeza).upper()
        dica = "Limpeza"
    elif numero_aleatorio == 4:
        palavra_secreta = random.choice(lista_animais).upper()
        dica = "Animal"

    tamanho = len(palavra_secreta)

    return palavra_secreta, dica, tamanho

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif(erros == 5):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif(erros == 4):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif(erros == 2):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif(erros == 1):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif (erros == 0):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    
    else:
        print(" |")
        print(" |")
        print(" |")
        print(" |")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor(palavra_secreta):
    os.system('clear')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
    print(f"Parabéns, você ganhou! A palavra era: {palavra_secreta}")

def imprime_mensagem_perdedor(palavra_secreta):
    os.system('clear')
    print("   ___   ___________     ")
    print("  /   \_/           \    ")
    print(" /                   \   ")
    print(" |    XX       XX    /   ")
    print("  \  XXXX     XXXX   \   ")
    print("  /   XX       XX    |   ")
    print(" \__       X       __/   ")
    print("   |\     XXX     /|     ")
    print("   | |           | |     ")
    print("   | | I I I I I | |     ")
    print("   \   I I I I I   /     ")
    print("    \__         __/      ")
    print("       \_______/         ")
    print(f"Você perdeu! A palavra era: {palavra_secreta}")

def mensagem_boas_vindas():
    print("***********************************")
    print("*   Bem-vindo ao jogo da Forca    *")
    print("***********************************")
    print()
    time.sleep(2)

def mensagem_jogo_iniciado():
    os.system('clear')
    print("***********************************")
    print("*          jogo da Forca          *")
    print("***********************************")
    print()

# Orientações ao jogador referente status da partida.
def informar_status_partida(tentativas,tamanho,dica,letras_acertadas):
    desenha_forca(tentativas)
    print(f"Possibilidades de erro restantes: {tentativas}")
    print()
    print(f"Uma palavra com {tamanho} letras!")
    print(f"Dica: {dica}")

    # Exibindo a lista de letras acertadas.
    print(" ".join(letras_acertadas))
    print()

# Solicitando input para o jogador, removendo espaços e convertendo em caixa alta.
def solicitar_input_jogador():
    chute_do_jogador = input("Informe uma letra: ").strip().upper()
    return chute_do_jogador

def iniciar_variaveis_ambiente_partida():
    # Iniciando variáveis de fim de jogo.
    venceu = False
    tentativas = 7

    # Ativando uma palavra Secreta e uma dica correspondente.
    palavra_secreta, dica, tamanho = sorteio_palavra_secreta()

    # Inicializando letras_acertadas com underscores.
    letras_acertadas = ["_"] * len(palavra_secreta)
    return venceu, tentativas, dica, tamanho, palavra_secreta, letras_acertadas

def gravar_letra_correta(palavra_secreta,chute_do_jogador,letras_acertadas):
    for i, letra in enumerate(palavra_secreta):
        if chute_do_jogador == letra:
            letras_acertadas[i] = letra
    return letras_acertadas

def validar_vitoria(letras_acertadas,venceu):
    # Se não houver mais underscores na String, significa que o jogador acertou todas.
    if "_" not in letras_acertadas:
        venceu = True
    return venceu

# Inicio do Programa.
def main():
    mensagem_boas_vindas()

    # lanço da partida principal.
    while True:
        venceu, tentativas, dica, tamanho, palavra_secreta, letras_acertadas = iniciar_variaveis_ambiente_partida()

        # lanço das tentativas do jogador.
        while tentativas > 0 and not venceu:
            mensagem_jogo_iniciado()

            informar_status_partida(tentativas,tamanho,dica,letras_acertadas)
            
            print()
            chute_do_jogador = solicitar_input_jogador()

            # Se o chute for correto, realiza um FOR para guardar a letra no indice correspondente.
            if chute_do_jogador in palavra_secreta:
                letras_acertadas = gravar_letra_correta(palavra_secreta,chute_do_jogador,letras_acertadas)
                print("Acertou a Letra!")
            else:
                tentativas -= 1
                print("Letra Incorreta!")
            
            time.sleep(2)
            venceu = validar_vitoria(letras_acertadas,venceu)

        # Validação final (Vitória ou Derrota).
        print()
        if venceu:
            imprime_mensagem_vencedor(palavra_secreta)
        else:
            desenha_forca(tentativas)
            imprime_mensagem_perdedor(palavra_secreta)

        nova_partida = input("Iniciar Nova Partida (S/N)? ").strip().lower()
        
        if nova_partida != "s":
            print("Fim de Jogo!")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()