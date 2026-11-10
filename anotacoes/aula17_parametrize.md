# Aula 17 - Entendendo pytest.mark.parametrize

## Decorators

Um decorator adiciona comportamento a uma
funcao sem alterar diretamente seu codigo.

## Pytest.mark.parametrize

Permite executar a mesma funcao de teste
com diferentes conjuntos de parametros.

## Beneficios

- Menos repeticao de codigo.
- Melhor organizacao dos testes.
- Facilidade de manutencao.
- Mais cenarios com uma unica funcao.

## Exemplo

@pytest.mark.parametrize(
    ("nota", "esperado"),
    [
        (100, True),
        (60, True),
        (59, False),
        (0, False),
    ],
)

## Conceitos

O Pytest coleta um teste para cada conjunto
de parametros fornecido pelo decorator.

## Arquivos

aulas/aula17_parametrize.py
tests/test_aula17_parametrize.py

## Observacao

Esta aula introduz o conceito.
As proximas aulas aprofundarao a implementacao.
