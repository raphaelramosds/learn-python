"""
Exemplo de um loop que executa duas tarefas de forma sincrona
"""
import time

def tarefa(nome):
    for i in range(3):
        print(f'{nome}: passo {i}')
        time.sleep(1)  # bloqueia ambas tarefas (B so executa depois de A)
        yield

def executar():
    t1 = tarefa('A')
    t2 = tarefa('B')
    for _ in range(3):
        next(t1)
        next(t2)

executar()