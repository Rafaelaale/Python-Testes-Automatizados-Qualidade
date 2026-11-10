"""Testes da Aula 15 - Complexidade ciclomática."""

import pytest

from aulas.aula15_complexidade import (
    classificar_nota_complexa,
    classificar_nota_refatorada,
)


@pytest.mark.parametrize(
    ("nota", "esperado"),
    [
        (100, "A"),
        (90, "A"),
        (85, "B"),
        (75, "C"),
        (65, "D"),
        (55, "E"),
        (45, "F"),
        (35, "G"),
        (25, "H"),
        (15, "I"),
        (5, "J"),
        (0, "J"),
    ],
)
def test_classificacoes_equivalentes(nota, esperado):
    """Verifica se as duas implementacoes concordam."""
    assert classificar_nota_complexa(nota) == esperado
    assert classificar_nota_refatorada(nota) == esperado
