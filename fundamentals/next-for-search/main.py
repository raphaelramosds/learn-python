"""
Uso de next() com for

O next() pode ser combinado com expressões geradoras (for ...) 
para encontrar rapidamente o primeiro elemento que satisfaça 
uma condição em uma estrutura de dados.

Vantagens:
- Evita criar listas intermediárias (diferente de usar list comprehensions).
- Itera apenas até encontrar o primeiro elemento válido, economizando memória e tempo.
- Permite definir um valor padrão caso nenhum item seja encontrado.
"""

animais = ['macaco', 'coelho', 'rato', 'cachorro']

animal_m = next((a for a in animais if a.startswith('c')), None)

print(animal_m)