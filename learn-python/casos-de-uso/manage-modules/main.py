"""
Uso do arquivo __init__.py em pacotes

O arquivo __init__.py é utilizado para:

1. Indicar que a pasta deve ser tratada como um pacote/módulo importável.
   (Em versões modernas do Python, nem sempre é obrigatório, mas continua sendo
   prática comum para organização de pacotes.)

2. Controlar o que é exposto ao importar o pacote.
   - Permite importar funções, classes ou variáveis diretamente, sem precisar
     conhecer a estrutura interna dos módulos.

Exemplo: Expor método calcular do módulo aritmetica
    Estrutura:
        aritmetica/
            __init__.py
            module.py

    Conteúdo de module.py:
        def calcular(x, y):
            return (x + y)/2

    Conteúdo de __init__.py:
        from .module import calcular
"""

import aritmetica as art
import geometrica as geo

print(art.calcular(10, 3))
print(geo.calcular(10, 3))