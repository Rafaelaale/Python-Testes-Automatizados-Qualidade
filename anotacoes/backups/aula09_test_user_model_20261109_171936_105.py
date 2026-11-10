"""Aula 07: testes unitarios da serializacao de usuario."""

import pytest
from models.user_model import serialize_user


def test_serialize_user_completo():
    """Valida todos os campos de um usuario completo."""
    usuario = {
        "email": "teste@exemplo.com",
        "name": "Teste Usuario",
        "address": "123 Rua Exemplo",
        "role": "admin",
    }

    resultado = serialize_user(usuario)

    assert resultado == usuario


def test_serialize_user_incompleto():
    """Valida os valores padrao dos campos ausentes."""
    usuario = {
        "email": "cliente@exemplo.com",
    }

    resultado = serialize_user(usuario)

    esperado = {
        "email": "cliente@exemplo.com",
        "name": "",
        "address": "",
        "role": "cliente",
    }

    assert resultado == esperado


def test_serialize_user_entrada_invalida():
    """Valida o erro ao receber inteiro no lugar de dict."""
    with pytest.raises(AttributeError):
        serialize_user(123)


def test_serialize_user_sem_email():
    """Verifica os valores padrao com dicionario vazio."""
    resultado = serialize_user({})

    esperado = {
        "email": None,
        "name": "",
        "address": "",
        "role": "cliente",
    }

    assert resultado == esperado


def test_serialize_user_string_invalida():
    """Verifica erro ao receber string em vez de dicionario."""
    with pytest.raises(AttributeError):
        serialize_user("usuario invalido")


def test_serialize_user_valores_inesperados():
    """Verifica que o serializador preserva valores incomuns."""
    usuario = {
        "email": 123456,
        "name": ["Nome Inesperado", "Outro Nome"],
        "address": {"rua": "123 Exemplo"},
        "role": True,
    }

    resultado = serialize_user(usuario)

    assert resultado == usuario
