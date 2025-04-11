# Faça um programa que solicite o preço de uma mercadoria e o
# percentual de desconto. Exiba o valor do desconto e o preço a pagar.

print("\nFaça um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.\n")


preco = float(input("Preço da mercadoria: "))

desconto = float(input("Percentual de desconto: ")) / 100

val_desc = preco * desconto
val_pag = (1 - desconto) * preco
print(f"Valor do desconto: {val_desc:.2f}")

print(f"Preço a pagar: {val_pag:.2f}")