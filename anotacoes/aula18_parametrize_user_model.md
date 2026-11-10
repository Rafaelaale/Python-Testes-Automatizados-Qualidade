# Aula 18 - Testes parametrizados do User Model

## Objetivo

Reduzir repeticao de codigo utilizando
@pytest.mark.parametrize.

## Arquivo criado

auth-service/test/test_user_model_parametrize.py

## Primeiro grupo: entradas validas

Cinco conjuntos de parametros:

1. Usuario completo.
2. Usuario incompleto.
3. Dicionario vazio.
4. Dicionario com todos os valores None.
5. Dicionario com tipos inesperados.

Cada conjunto possui:
- user: entrada
- esperado: resultado esperado

## Segundo grupo: entradas invalidas

Quatro conjuntos de parametros:

- None
- String
- Inteiro
- Lista

Excecao esperada:
AttributeError

## Conceitos

@pytest.mark.parametrize
pytest.param
pytest.raises
assert

## Diferenca importante

Chave ausente utiliza o valor padrao.

Chave existente com None preserva None.

## Ganho de produtividade

Duas funcoes parametrizadas representam
nove cenarios de teste.

Os nove testes anteriores foram preservados.

## Validacao

A verificacao unitária utiliza addopts vazio
para nao aplicar a meta geral de cobertura
de 80% da Aula 12.

A medicao de cobertura isolada analisa
somente models.user_model.

## Arquivos de resultados

resultados/aula18_parametrize/
