# Escreva um programa que peça números ao usuário até que ele digite
# 0. Ao final, imprima a soma de todos os números digitados.

print("\nQuando digitar 0 o looping para.\n")
soma = 0

while (valor := int(input("Digite um número inteiro: "))) != 0:
    soma += valor

print(f"Soma de todos os números digitados: {soma}")