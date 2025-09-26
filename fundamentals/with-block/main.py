"""
Uso do bloco with em Python

O bloco `with` é utilizado para gerenciar recursos e controlar contextos 
de forma segura, seguindo o "context manager protocol".

Esse protocolo é implementado por classes que definem os métodos mágicos:
- __enter__(self): executado ao entrar no contexto (início do bloco).
- __exit__(self, exc_type, exc_value, traceback): executado ao sair do contexto,
  mesmo que ocorra uma exceção dentro do bloco.
"""


class Foo:
    
    def __exit__(self, *args):
        print("Saindo do bloco with")
        print(args)

    def __enter__(self):
        print("Entrando no bloco with")
        return ["inicio"]


x = 10
foo = Foo()
with foo as retorno:
    print("Dentro do bloco")
    x = 2
    print(retorno)

print(x)  # saida: x = ?
