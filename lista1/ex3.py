# Escreva um programa que pergunte a velocidade do carro de um
# usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi
# multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80
# km/h.

print("\nEscreva um programa que pergunte a velocidade do carro de um usuário. \nCaso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. \nNesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.\n")

velocidade = float(input("Velocidade do carro(km/h): "))

if velocidade > 80:
    print(f"Você foi multado em R${(velocidade - 80) * 5:.2f}")
else:
    print("Tudo certo!")


