"""Aula 13: exemplos de analise estatica com Pylint."""

import math


def calcular_total(valor, quantidade):
    resultado = valor * quantidade
    temporario = 100
    return resultado


def mostrar_total():
    total = calcular_total(10, 3)
    print(total)


if __name__ == "__main__":
    mostrar_total()
