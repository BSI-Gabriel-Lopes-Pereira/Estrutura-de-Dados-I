def fatorial_loop(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def fatorial_recursivo(n):
    if n == 0:
        return 1
    return n * fatorial_recursivo(n - 1)