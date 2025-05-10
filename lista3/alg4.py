def busca_linear(lista, valor):
    for item in lista:
        if item == valor:
            return True
    return False

def busca_in(lista, valor):
    return valor in lista