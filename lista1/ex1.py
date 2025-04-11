# Escreva um programa que leia a quantidade de dias, horas, minutos e
# segundos do usuário. Calcule o total em segundos.

print("\nEx1 - Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.\n")

dias = int(input("Quantidade de dias: ")) # 1d = 86400
horas = int(input("Quantidade de horas: ")). # 1h = 3600
minutos = int(input("Quantidade de minutos: ")) # 1m = 60
segundos = int(input("Quantidade de segundos: "))

total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos

print(f"Total de segundos: {total:,}".replace(",", "."))