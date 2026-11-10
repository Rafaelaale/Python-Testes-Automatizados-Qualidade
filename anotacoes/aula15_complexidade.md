# Aula 15 - Complexidade ciclomática

## Objetivo

Entender como decisões e caminhos lógicos
influenciam a complexidade do código.

## Ferramenta

Radon - análise estática de código Python.

## Comando

python -m radon cc arquivo.py -s -a

## Parâmetros

cc - Calcula complexidade ciclomática.
-s - Exibe a pontuação numérica.
-a - Exibe a média da complexidade.

## Experimento

Comparar duas implementações de
classificação de notas.

Uma utiliza vários if/elif.
A outra utiliza uma tabela de limites.

## Testes

Pytest verifica a equivalência das saídas.

## Importante

Menor complexidade não garante
automaticamente código correto.

## Relatórios

resultados/aula15_complexidade/exemplo.txt
resultados/aula15_complexidade/controller.txt

## Segurança

O código original da hamburgueria
não foi modificado.
