# Calcular Índice de Massa Corporal

import os
import time

while True:

    while True:
        
        print()
        try: 
            altura = float(input("Altura: "))
            peso = float(input("Peso: "))
            break
        except:
            print("Utilize ponto ao invés de virgula.")
            time.sleep(3)
            os.system('clear')

    altura_exponencial = pow(altura, 2)

    peso_ideal_menor = (18.5 * altura_exponencial)
    peso_ideal_medio = (21.7 * altura_exponencial)
    peso_ideal_maior = (24.9 * altura_exponencial)

    peso_ideal_menor = round(peso_ideal_menor,1)
    peso_ideal_medio = round(peso_ideal_medio,1)
    peso_ideal_maior = round(peso_ideal_maior,1)

    indice_IMC=(peso/altura_exponencial)
    indice_IMC = round(indice_IMC,1)

    print()
    print("Seu índice IMC é: ",indice_IMC)

    if indice_IMC < 18.5:
        print("Você está abaixo do peso.")
        
    elif 18.5 <= indice_IMC < 24.9:
        print("Você está com peso normal.")
        
    elif 24.9 <= indice_IMC < 29.9:
        print("Você está com sobrepeso.")
        
    else:
        print("Você está com Obesidade")

    print()
    print("Mantenha seu peso entre:")
    print("(Minimo):",peso_ideal_menor," Kg")
    print("(Medio) :",peso_ideal_medio," Kg")
    print("(Maximo):",peso_ideal_maior," Kg")
    
    print()
    reiniciar = input("Realizar novo calculo (S/N)? ").strip().lower()
    
    os.system('clear')

    if reiniciar != "s":
        break

