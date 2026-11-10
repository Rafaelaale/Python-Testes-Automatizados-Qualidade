"""Aula 06 - Testes HTTP dos quatro microservicos Flask."""

import pytest
import requests

SERVICOS = [
    ("auth-service", 5000, "/auth/login"),
    ("user-service", 5001, "/user/create"),
    ("order-service", 5002, "/"),
    ("product-service", 5003, "/product/list"),
]


@pytest.mark.parametrize("nome,porta,rota", SERVICOS)
def test_microservico_responde_http(nome, porta, rota):
    url = f"http://127.0.0.1:{porta}{rota}"

    resposta = requests.get(
        url,
        timeout=10,
        allow_redirects=False,
    )

    assert resposta.status_code in (200, 301, 302, 303, 307, 308), (
        f"{nome}: HTTP {resposta.status_code}"
    )
