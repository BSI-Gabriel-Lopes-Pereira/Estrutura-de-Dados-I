# Escreva um programa para aprovar o empréstimo bancário para
# compra de uma casa. O programa deve perguntar o valor da casa a comprar, o
# salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser
# superior a 30% do salário. Calcule o valor da prestação como sendo o valor da
# casa a comprar dividido pelo número de meses a pagar.

val_casa = float(input("Valor da casa a comprar: "))

salario = float(input("Seu salário: "))

qtd_meses_a_pagar = int(input("Quantidade de anos a pagar: ")) * 12

val_prest = val_casa / qtd_meses_a_pagar

trint_porcen_sal = salario * 0.3
if val_prest > trint_porcen_sal:
    print("Negado! O valor da prestação mensal não pode ser superior a 30% do salário.")
else:
    print(f"Aprovado! O valor da prestação será de {val_prest:.2f}")