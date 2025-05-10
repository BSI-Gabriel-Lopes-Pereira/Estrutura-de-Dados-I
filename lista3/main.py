import timeit

from alg1 import soma_numeros_loop, soma_numeros_formula
from alg2 import eh_primo_simples, eh_primo_otimizado
from alg3 import reverter_string_loop, reverter_string_slice
from alg4 import busca_linear, busca_in
from alg5 import fatorial_loop, fatorial_recursivo

def executar_testes():
    resultados = {
        "Soma de N Números - Loop": timeit.timeit('soma_numeros_loop(1000)', globals=globals(), number=1000),
        "Soma de N Números - Fórmula": timeit.timeit('soma_numeros_formula(1000)', globals=globals(), number=1000),
        "Verificação de Primo - Simples": timeit.timeit('eh_primo_simples(997)', globals=globals(), number=1000),
        "Verificação de Primo - Otimizado": timeit.timeit('eh_primo_otimizado(997)', globals=globals(), number=1000),
        "Reversão de String - Loop": timeit.timeit('reverter_string_loop("abcdefghijklmnopqrstuvwxyz")', globals=globals(), number=1000),
        "Reversão de String - Slicing": timeit.timeit('reverter_string_slice("abcdefghijklmnopqrstuvwxyz")', globals=globals(), number=1000),
        "Busca em Lista - Linear": timeit.timeit('busca_linear(list(range(1000)), 999)', globals=globals(), number=1000),
        "Busca em Lista - Operador 'in'": timeit.timeit('busca_in(list(range(1000)), 999)', globals=globals(), number=1000),
        "Fatorial - Loop": timeit.timeit('fatorial_loop(10)', globals=globals(), number=1000),
        "Fatorial - Recursivo": timeit.timeit('fatorial_recursivo(10)', globals=globals(), number=1000),
    }
    return resultados

resultados_teste = executar_testes()
for descricao, tempo in resultados_teste.items():
    print(f"{descricao}: {tempo:.6f} segundos")
