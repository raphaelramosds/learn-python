"""
Corrotinas e Funções Geradoras

Tanto corrotinas (async def) quanto geradores (yield) permitem pausar e retomar uma função, 
mas as corrotinas são voltadas para execução assíncrona (I/O não bloqueante com event loop), 
enquanto os geradores servem para produzir dados sob demanda de forma síncrona.
"""

import asyncio
import time

async def corrotina():
    print('hello')
    await asyncio.sleep(1)
    print('world')

# Executar corrotina assíncrona com asyncio
print('chamou corrotina')
asyncio.run(corrotina())
print('executado')

def gerador():
    print('hello do gerador')
    time.sleep(1)
    print('world do gerador')
    yield

# Executar Função geradora
func = gerador()
next(func) # Executa até o primeiro yield