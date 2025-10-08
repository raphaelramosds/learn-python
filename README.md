# Aprender Python

## Visão geral

Este repositório reúne exemplos de código que exploram conceitos da linguagem **Python** e suas principais ferramentas.

### [Fundamentos](./learn-python/fundamentals/)  

- [Bloco with](./learn-python/fundamentals/with-block/)
- [Corrotinas e Funções Geradoras](./learn-python/fundamentals/couroutines-generators/)
- [Padrões WSGI e ASGI](learn-python/fundamentals/wsgi-asgi)

### [Ferramentas](./learn-python/tools/)  

- [MyPy](./learn-python/tools/mypy/)

### [Casos de uso](./learn-python/casos-de-uso/)

- [Busca linear com next() e for](./learn-python/casos-de-uso/next-for-search/)
- [Exposição de módulos e controle de namespaces com __init__.py](./learn-python/casos-de-uso/manage-modules/)

## Poetry

Esse repositório utiliza o Poetry para gerenciar as dependências.

> Certifique-se de instalar e configurar o Poetry corretamente. Siga as instruções em [Poetry: instalação e configuração](https://github.com/raphaelramosds/huggingface-llm-course/blob/main/docs/poetry/README.md)

```shell
# Instale as dependencias
poetry install

# Entre no ambiente virtual
source $(poetry env info --path)/bin/activate
```