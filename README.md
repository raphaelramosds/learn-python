# Aprender Python

## Visão geral

Este repositório reúne exemplos de código que exploram conceitos da linguagem **Python** e suas principais ferramentas.

### [Fundamentos](./learn-python/fundamentals/)  

- [Uso do arquivo __init__.py em pacotes](./learn-python/fundamentals/manage-modules/)
- [Uso de next() com for](./learn-python/fundamentals/next-for-search/)
- [Uso do bloco with](./learn-python/fundamentals/with-block/)

### [Ferramentas](./learn-python/tools/)  

- [MyPy](./learn-python/tools/mypy/)

## Poetry

Esse repositório utiliza o Poetry para gerenciar as dependências.

> Certifique-se de instalar e configurar o Poetry corretamente. Siga as instruções em [Poetry: instalação e configuração](https://github.com/raphaelramosds/huggingface-llm-course/blob/main/docs/poetry/README.md)

```shell
# Instale as dependencias
poetry install

# Entre no ambiente virtual
source $(poetry env info --path)/bin/activate
```