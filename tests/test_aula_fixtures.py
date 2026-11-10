import pytest


@pytest.fixture(scope="function")
def preparar_dados():
    print("\nSETUP: preparando dados ficticios")

    dados = {
        "nome": "Cliente Teste",
        "saldo": 1000,
    }

    yield dados

    print("\nTEARDOWN: finalizando ambiente")


def test_saldo_inicial(preparar_dados):
    assert preparar_dados["saldo"] == 1000


@pytest.fixture
def preparar_ambiente():
    print("\nSETUP: ambiente preparado")

    yield

    print("\nTEARDOWN: ambiente finalizado")


@pytest.mark.usefixtures("preparar_ambiente")
def test_operacao():
    assert 10 + 5 == 15