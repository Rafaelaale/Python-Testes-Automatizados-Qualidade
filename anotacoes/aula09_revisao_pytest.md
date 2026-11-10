# Aula 09 - Revisando testes unitarios com Pytest

## Funcao estudada

serialize_user(user)

Microservico: auth-service

## Novos cenarios

1. Lista como entrada: AttributeError.
2. None como entrada: AttributeError.
3. Dicionario com valores None: preserva None.

## Diferenca fundamental

Chave ausente:
user.get("name", "") retorna "".

Chave presente com None:
user.get("name", "") retorna None.

## Ferramentas e conceitos

- pytest.raises
- assert
- Testes de excecoes
- Testes de valores nulos
- Testes de regressao
- pytest -v
- Ruff para qualidade

## Observacoes

O exemplo do material da aula apresenta valores
padrao para um dicionario com chaves explicitamente
definidas como None.

O codigo original nao funciona dessa maneira.
Os testes documentam o comportamento verdadeiro.

Nenhum codigo original da aplicacao foi alterado.
