"""
Exemplo de uso do MyPy para verificação estática de tipos em Python.

Instalação:
    pip install mypy

Configuração:
    O arquivo `mypy.ini` define regras específicas do MyPy para o projeto,
    como diretórios a serem ignorados, opções de tipo estrito e exclusões.

Verificação de um arquivo específico:
    mypy main.py

Verificação de todos os arquivos em um diretório:
    mypy tools/

Observações:
    - O MyPy não executa o código; ele apenas analisa os tipos.
    - O Python NÃO lança exceções de verificação de tipos em tempo de execução.
    - Isso pode gerar bugs sutis, como tratar uma string como float sem erro imediato.
    - Executar o MyPy antes de enviar o código para produção ajuda a prevenir esses problemas.
"""

# Tipagem dinamica: tipos inferidos pela linguagem
def add_numbers(a, b):
    return a + b

# Tipagem estatica: tipos definidos
def add_numbers_v2(a: int, b: int) -> int:
    return a + b

result = add_numbers(5, 3)

try:
    result_v2 = add_numbers_v2("5", 3)
except TypeError as tp:
    print(tp)