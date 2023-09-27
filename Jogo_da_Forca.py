# Classico jogo da Forca, tente adivinhar a palavra em até 7 tentativas

import os
import time

## JOGO EM FASE DE DESENVOLVIMENTO

def main():
    print("***********************************")
    print("*   Bem vindo ao jogo da Forca    *")
    print("***********************************")

    # Animação de Aguarde.
    time.sleep(1)
    print() 

    # Palavra secreta sempre será em caixa alta.
    palavra_secreta = "Banana"
    palavra_secreta = palavra_secreta.upper()

    # iniciando variáveis de fim de jogo.
    enforcou = False
    venceu = False

    while not enforcou and not venceu:

        #Solicita input para o usuário, remove espaços e converte em caixa alta.
        chute_usuario = input("Informe uma letra para adivinhar a Palavra: ").strip().upper()

        exibicao = ""
        for letra in palavra_secreta:
            
            if chute_usuario == letra:
                exibicao = exibicao + letra
            else:
                exibicao = exibicao + " _ "
            
        print(exibicao)
            
    
    time.sleep(2)

if __name__ == "__main__":
    main()
