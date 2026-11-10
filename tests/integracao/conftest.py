import pytest
import requests
from unittest.mock import patch, Mock


@pytest.fixture
def base_url():
    """URLs dos quatro microsservicos."""
    return {
        "auth_url": "http://localhost:5000/auth",
        "user_url": "http://localhost:5001/user",
        "order_url": "http://localhost:5002/order",
        "product_url": "http://localhost:5003/product",
    }


@pytest.fixture
def sample_user():
    """Usuario ficticio para os testes."""
    return {
        "email": "cliente@teste.com",
        "password": "senha123",
        "name": "Cliente Teste",
        "address": "Rua Teste, 123",
        "role": "cliente",
    }


@pytest.fixture
def sample_items():
    """Itens ficticios de um pedido."""
    return {
        "item_name": ["Hambúrguer Teste", "Refrigerante Teste"],
        "item_price": [10.0, 5.0],
        "quantity": ["2", "1"],
    }


@pytest.fixture
def mock_user_service():
    """Simula a consulta ao servico de usuarios."""
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "email": "cliente@teste.com",
            "name": "Cliente Teste",
            "address": "Rua Teste, 123",
            "role": "cliente",
        }
        mock_get.return_value = mock_response
        yield mock_get


@pytest.fixture
def mock_order_service():
    """Simula a criacao de pedidos com redirecionamento."""
    with patch("requests.post") as mock_post:
        mock_response = Mock()
        mock_response.status_code = 302
        mock_response.headers = {"location": "/order/list"}
        mock_post.return_value = mock_response
        yield mock_post


def check_service_health(url):
    """Verifica a disponibilidade HTTP de um servico."""
    try:
        response = requests.get(f"{url}/", timeout=2)
        return response.status_code in (200, 302, 404)
    except requests.exceptions.RequestException:
        return False

# AULA - CRIANDO CASOS DE TESTE

@pytest.fixture
def base_urls(base_url):
    """Adapta as URLs existentes aos nomes usados nesta aula."""
    return {
        "auth": base_url["auth_url"],
        "user": base_url["user_url"],
        "order": base_url["order_url"],
        "product": base_url["product_url"],
    }


@pytest.fixture
def services_running(base_urls):
    """Verifica a disponibilidade dos quatro servicos."""
    return {
        service: check_service_health(url)
        for service, url in base_urls.items()
    }


@pytest.fixture
def skip_if_services_down(services_running):
    """Pula testes que dependem de servicos indisponiveis."""
    def verificar(*required_services):
        for service in required_services:
            if not services_running.get(service, False):
                pytest.skip(
                    f"Servico {service} nao esta disponivel"
                )

    return verificar