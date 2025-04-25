# Questão 3: Adicione uma nova chave 'profissão' ao dicionário pessoa com o valor
# 'Engenheira'.

from ex1 import pessoa

pessoa['profissão'] = 'Engenheira'

print(pessoa)
print(f'A profissão da pessoa é: {pessoa["profissão"]}')