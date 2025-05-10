def soma_numeros_loop(n):
    soma = 0
    for i in range(1, n + 1):
        soma += i
    return soma

def soma_numeros_formula(n):
    return n * (n + 1) // 2