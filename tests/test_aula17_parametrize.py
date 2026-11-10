"""Aula 17: testes com pytest.mark.parametrize."""

import pytest

from aulas.aula17_parametrize import verificar_aprovacao


@pytest.mark.parametrize(
    ("nota", "esperado"),
    [
        (100, True),
        (60, True),
        (59, False),
        (0, False),
    ],
)
def test_verificar_aprovacao(nota, esperado):
    """Executa quatro cenarios usando uma unica funcao."""
    assert verificar_aprovacao(nota) == esperado
