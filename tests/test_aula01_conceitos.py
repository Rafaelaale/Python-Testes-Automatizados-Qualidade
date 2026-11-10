import pytest

from src.calculadora import somar
from src.operacoes_integradas import (
    multiplicar,
    multiplicar_e_somar,
)


@pytest.mark.parametrize(
    "a,b,esperado",
    [
        (2, 3, 5),
        (-2, -3, -5),
        (-5, 3, -2),
        (0, 0, 0),
    ],
)
def test_soma_unitaria(a, b, esperado):
    assert somar(a, b) == esperado


def test_multiplicacao_unitaria():
    assert multiplicar(4, 3) == 12


def test_integracao_multiplicacao_e_soma():
    assert multiplicar_e_somar(4, 3, 5) == 17


def test_regressao_soma_original():
    assert somar(10, 20) == 30
