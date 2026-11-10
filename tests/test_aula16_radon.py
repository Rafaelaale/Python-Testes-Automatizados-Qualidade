"""Testes da Aula 16: login simulado."""

import pytest

from aulas.aula16_radon.complexidade import login_complexo


@pytest.mark.parametrize(
    ("usuario", "senha", "esperado"),
    [
        (None, "senha_teste", "usuario_invalido"),
        ("alura", None, "senha_invalida"),
        ("", "senha_teste", "usuario_invalido"),
        ("bloqueado_01", "senha_teste", "bloqueado"),
        ("alura", "senha_teste", "autenticado"),
        ("alura", "errada", "credenciais_invalidas"),
    ],
)
def test_login_complexo(usuario, senha, esperado):
    """Verifica resultados do login simulado."""
    assert login_complexo(usuario, senha) == esperado
