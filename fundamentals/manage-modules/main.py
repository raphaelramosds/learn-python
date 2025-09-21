"""
O arquivo __init__.py é utilizado para:

  - Indicar que a pasta é um pacote/módulo que pode ser importado
  - Expor funções/classes diretamente 
    Ex: nao precisamos saber que o metodo calcular esta definido dentro de aritmetica/module.py pois ele foi exposto no arimetica/__init__.py
    
"""

import aritmetica as art
import geometrica as geo

print(art.calcular(10, 3))
print(geo.calcular(10, 3))