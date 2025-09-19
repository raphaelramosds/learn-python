# O bloco `with` é utilizado para controlar contextos no seu programa com o "context manager protocol"
# NOTE: classes que serao utilizadas como contexto possuem os metodos magicos __exit__ e __enter__


class Foo:

    def __exit__(self, *args):
        print("Saindo do bloco with")
        print(args)

    def __enter__(self):
        print("Entrando no bloco with")


x = 10
foo = Foo()
with foo:
    print("Dentro do bloco")
    x = 2

print(x)  # saida: x = ?
