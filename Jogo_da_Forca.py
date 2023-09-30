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
    lista_tecnologia = ['COMPUTADOR','TECLADO','CELULAR','CRIPTOMOEDA','IMPRESSORA','CAMERA','INTERNET']
    lista_limpeza = ['SABONETE','AMACIANTE','SHAMPOO','ESPONJA','PANO','VASSOURA']
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

# Inicio do Programa.
def main():
    print("***********************************")
    print("*   Bem-vindo ao jogo da Forca    *")
    print("***********************************")
    print()

    time.sleep(1)

    # lanço da partida principal.
    while True:
        
        # Ativando uma palavra Secreta e uma dica correspondente.
        palavra_secreta, dica, tamanho = sorteio_palavra_secreta()

        # Inicializando letras_acertadas com underscores.
        letras_acertadas = ["_"] * len(palavra_secreta)

        # Iniciando variáveis de fim de jogo.
        venceu = False
        tentativas = 7

        # lanço das tentativas do jogador.
        while tentativas > 0 and not venceu:
            
            os.system('clear')

            print("***********************************")
            print("*          jogo da Forca          *")
            print("***********************************")
            print()

            # Orientações ao jogador.
            print(f"Possibilidades de erro restantes: {tentativas}")
            print()
            print(f"Uma palavra com {tamanho} letras!")
            print(f"Dica: {dica}")
            print()

            # Exibindo a lista de letras acertadas.
            print(" ".join(letras_acertadas))

            # Solicitando input para o jogador, removendo espaços e convertendo em caixa alta.
            print()
            chute_do_jogador = input("Informe uma letra: ").strip().upper()

            # Se o chute for correto, realiza um FOR para guardar a letra no indice correspondente.
            if chute_do_jogador in palavra_secreta:
                for i, letra in enumerate(palavra_secreta):
                    if chute_do_jogador == letra:
                        letras_acertadas[i] = letra
                print("Acertou a Letra!")
            else:
                tentativas -= 1
                print("Letra Incorreta!")
            
            time.sleep(2)

            # Se não houver mais underscores na String, significa que o jogador acertou todas.
            if "_" not in letras_acertadas:
                venceu = True

        # Validação final (Vitória ou Derrota).
        print()
        if venceu:
            print(f"Parabéns, você ganhou! A palavra era: {palavra_secreta}")
        else:
            print(f"Você perdeu! A palavra era: {palavra_secreta}")

        nova_partida = input("Iniciar Nova Partida (S/N)? ").strip().lower()
        
        if nova_partida != "s":
            print("Fim de Jogo!")
            time.sleep(2)
            break

if __name__ == "__main__":
    main()