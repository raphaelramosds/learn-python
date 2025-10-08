# Interfaces de comunicação entre servidores em Python

As interfaces WSGI e ASGI são padrões utilizados para estabelecer a comunicação entre servidores e frameworks em Python.

- [WSGI (PEP-333)](https://peps.python.org/pep-0333/)
- [ASGI](https://asgi.readthedocs.io/en/latest/)

Servidores que implementam a interface ASGI incluem: 

- [uvicorn](https://www.uvicorn.org/)
- [daphne](https://github.com/django/daphne/)
- [hypercorn](https://hypercorn.readthedocs.io/en/latest/)

Alguns frameworks compatíveis com ASGI são:

- [Starlette](https://www.starlette.dev/)
- [FastAPI](https://fastapi.tiangolo.com/)