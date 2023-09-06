
altura = float(input("Altura: "))
peso = float(input("Peso: "))

exponencial = pow(altura, 2)

indiceIMC=(peso/exponencial)
indiceIMC = round(indiceIMC,1)


print()
print("Seu índice IMC é: ",indiceIMC)

if indiceIMC < 18.5:
    print("Você está abaixo do peso.")
    print("Consulte um nutricionista!")
elif 18.5 <= indiceIMC < 24.9:
    print("Você está normal.")
    print("Continue assim!")
elif 24.9 <= indiceIMC < 29.9:
    print("Você está com sobrepeso.")
    print("Faça execicios regularmente!")
else:
    print("Você está com Obesidade")
    print("Consulte um nutricionista e vá para a academia.")
