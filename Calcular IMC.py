
while True:

    print()
    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    alturaExponencial = pow(altura, 2)

    pesoIdealMenor = (18.5 * alturaExponencial)
    pesoIdealMedio = (21.7 * alturaExponencial)
    pesoIdealMaior = (24.9 * alturaExponencial)

    pesoIdealMenor = round(pesoIdealMenor,1)
    pesoIdealMedio = round(pesoIdealMedio,1)
    pesoIdealMaior = round(pesoIdealMaior,1)

    indiceIMC=(peso/alturaExponencial)
    indiceIMC = round(indiceIMC,1)

    print()
    print("Seu índice IMC é: ",indiceIMC)

    if indiceIMC < 18.5:
        print("Você está abaixo do peso.")
        
    elif 18.5 <= indiceIMC < 24.9:
        print("Você está com peso normal.")
        
    elif 24.9 <= indiceIMC < 29.9:
        print("Você está com sobrepeso.")
        
    else:
        print("Você está com Obesidade")

    print()
    print("Mantenha seu peso entre:")
    print("(Minimo):",pesoIdealMenor," Kg")
    print("(Medio) :",pesoIdealMedio," Kg")
    print("(Maximo):",pesoIdealMaior," Kg")
    
    print()
    reiniciar = input("Realizar novo calculo (S/N)? ").strip().lower()
    if reiniciar != "s":
        break

