from unittest.mock import Mock

import pytest


@pytest.fixture
def servicos_simulados():
    autenticacao = Mock()
    produtos = Mock()
    pedidos = Mock()

    autenticacao.login.return_value = {"token": "token_teste"}
    produtos.listar.return_value = [
        {"id": 1, "nome": "Hamburguer", "preco": 25.0}
    ]
    pedidos.criar.return_value = {
        "pedido_id": 101,
        "status": "criado",
    }

    return autenticacao, produtos, pedidos


def test_integracao_fluxo_pedido(servicos_simulados):
    autenticacao, produtos, pedidos = servicos_simulados

    sessao = autenticacao.login("cliente@teste.com", "senha_teste")
    catalogo = produtos.listar(token=sessao["token"])

    resultado = pedidos.criar(
        produto_id=catalogo[0]["id"],
        token=sessao["token"],
    )

    assert sessao["token"] == "token_teste"
    assert catalogo[0]["preco"] == 25.0
    assert resultado["status"] == "criado"

    autenticacao.login.assert_called_once()
    produtos.listar.assert_called_once_with(token="token_teste")
    pedidos.criar.assert_called_once_with(
        produto_id=1,
        token="token_teste",
    )


@pytest.mark.parametrize(
    "produto_id, status_esperado",
    [
        (1, "criado"),
        (2, "criado"),
        (3, "criado"),
    ],
)
def test_pedidos_parametrizados(produto_id, status_esperado):
    pedidos = Mock()
    pedidos.criar.return_value = {"status": status_esperado}

    resultado = pedidos.criar(produto_id=produto_id)

    assert resultado["status"] == status_esperado
    pedidos.criar.assert_called_once_with(produto_id=produto_id)