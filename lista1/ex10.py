# Faça um programa que calcule o aumento de um salário. Ele deve
# solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento
# e do novo salário.

salario_atual = float(input("Valor do salário atual: "))

porcentagem_aumento = float(input("Porcentagem do aumento: ")) / 100

print(f"Valor do aumento: R${salario_atual * porcentagem_aumento:.2f}")
print(f"Valor do novo salário: R${(1 + porcentagem_aumento) * salario_atual:.2f}")