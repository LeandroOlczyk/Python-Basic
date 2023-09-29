import os
import time

def main():
    print("***********************************")
    print("*   Bem-vindo ao jogo da Forca    *")
    print("***********************************")
    print()

    time.sleep(1)

    # Palavra secreta sempre será em caixa alta.
    palavra_secreta = "aguardente".upper()

    # Inicializando letras_acertadas com underscores
    letras_acertadas = ["_"] * len(palavra_secreta)

    tamanho = len(palavra_secreta)
    print(f"Uma palavra com {tamanho} letras! ")

    # Iniciando variáveis de fim de jogo.
    venceu = False
    tentativas = 7

    while tentativas > 0 and not venceu:
        # Exibindo a lista de letras acertadas
        print(" ".join(letras_acertadas))

        # Solicitando input para o usuário, removendo espaços e convertendo em caixa alta.
        chute_usuario = input("Informe uma letra: ").strip().upper()

        if chute_usuario in palavra_secreta:
            for i, letra in enumerate(palavra_secreta):
                if chute_usuario == letra:
                    letras_acertadas[i] = letra
            print(f"Parabéns, acertou a letra {chute_usuario}")
        else:
            tentativas -= 1
            print(f"Não foi dessa vez. Restam {tentativas} tentativas!")

        print()

        if "_" not in letras_acertadas:
            venceu = True

    if venceu:
        print(f"Parabéns, você ganhou! A palavra era: {palavra_secreta}")
    else:
        print(f"Você perdeu! A palavra era: {palavra_secreta}")

    time.sleep(5)

if __name__ == "__main__":
    main()