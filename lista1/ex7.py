# Crie uma tupla (0, 1, 2, 3, 4, 5, 6, 7, 8, 9) e imprima uma
# fatia com os elementos de índice 2 a 7 e outra com os elementos das posições pares.

tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

fatia1 = tupla[2:8]

fatia2 = tupla[::2]

print(f"Fatia com elementos de índice 2 a 7: {fatia1}")
print(f"Fatia com pares: {fatia2}")