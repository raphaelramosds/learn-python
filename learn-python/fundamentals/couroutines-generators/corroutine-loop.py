"""
Exemplo de um loop que executa duas tarefas de forma assincrona
"""

import asyncio

async def tarefa(nome):
    for i in range(3):
        print(f'{nome}: passo {i}')
        await asyncio.sleep(1)  # pausa só essa tarefa (B nao espera A, e vice-versa)

async def main():
    await asyncio.gather(tarefa('A'), tarefa('B'))

asyncio.run(main())