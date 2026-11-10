# Aula 16 - Analise de complexidade com Radon

## Objetivo

Medir a complexidade de uma funcao de login
propositalmente dificil de manter.

## Comandos

python -m radon cc complexidade.py -s -a
python -m radon mi complexidade.py -s
python -m radon hal complexidade.py
python -m radon raw complexidade.py

## Metricas

CC: complexidade ciclomática.
MI: indice de manutenibilidade.
Halstead: operadores, operandos, volume,
dificuldade, esforco e tempo estimado.
RAW: linhas fisicas, logicas, comentarios
e linhas em branco.

## Classificacao CC

A: 1 a 5
B: 6 a 10
C: 11 a 20
D: 21 a 30
E: 31 a 40
F: 41 ou mais

## Observacoes

Alta complexidade pode dificultar testes,
leitura e manutencao do codigo.

Uma nota MI alta nao anula problemas de CC.

As metricas de Halstead sao estimativas
matematicas, nao medidas reais de tempo humano.

O exemplo utiliza login simulado.
Os microservicos originais foram preservados.

## Relatorios

resultados/aula16_radon/
