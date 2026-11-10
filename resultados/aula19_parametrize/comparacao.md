# Aula 19 - Comparacao de testes

| Metrica | Tradicional | Parametrizado |
|---|---:|---:|
| Funcoes | 9 | 2 |
| Cenarios | 9 | 9 |
| Linhas | 109 | 97 |
| Instrucoes assert | 5 | 1 |

Reducao de funcoes: 77.8%
Diferenca de linhas: 12

## Interpretacao

A parametrizacao concentra varios cenarios
em menos funcoes de teste.

Uma reducao na quantidade de funcoes
nao implica necessariamente menos linhas.

Os dois arquivos permanecem preservados.

As contagens de cenarios sao estaticas;
o Pytest confirma a coleta e execucao.
