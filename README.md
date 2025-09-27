# Aprender Python

Este repositório reúne exemplos de código que exploram conceitos da linguagem **Python** e suas principais ferramentas.

## Organização

- [**Fundamentos**](./fundamentals/)  
  Exemplos sobre programação estruturada e orientação a objetos nativa da linguagem.

- [**Ferramentas**](./tools/)  
  Demonstra o uso de pacotes importantes do ecossistema Python, como `mypy`, `SQLAlchemy`, `pytest`, entre outros.

## Observações

Esse repositório utiliza o Poetry para gerenciar as dependências.

> Certifique-se de instalar e configurar o Poetry corretamente. Siga as instruções em [Poetry: instalação e configuração](https://github.com/raphaelramosds/huggingface-llm-course/blob/main/docs/poetry/README.md)

```shell
# Instale as dependencias
poetry install

# Entre no ambiente virtual
source $(poetry env info --path)/bin/activate
```