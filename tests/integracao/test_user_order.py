import pytest
import requests
from unittest.mock import patch, Mock


class TestOrderUserIntegration:

    def test_user_order_valid_user_with_services(
        self,
        base_urls,
        sample_user,
        sample_items,
        skip_if_services_down,
    ):
        """Pedido com usuario valido e servicos reais."""
        skip_if_services_down("user", "order")

        order_data = {
            "user_email": sample_user["email"],
            **sample_items,
        }

        response = requests.post(
            f"{base_urls['order']}/create",
            json=order_data,
            allow_redirects=False,
            timeout=5,
        )

        assert response.status_code == 302

    @patch("requests.post")
    def test_create_order_valid_user_mocked(
        self,
        mock_post,
        base_urls,
        sample_user,
        sample_items,
    ):
        """Criacao de pedido simulada com Mock."""
        mock_response = Mock()
        mock_response.status_code = 302
        mock_response.headers = {
            "Location": "/order/list"
        }

        mock_post.return_value = mock_response

        order_data = {
            "email": sample_user["email"],
            **sample_items,
        }

        response = requests.post(
            f"{base_urls['order']}/create",
            json=order_data,
            allow_redirects=False,
        )

        assert response.status_code == 302
        assert response.headers["Location"] == "/order/list"

        mock_post.assert_called_once_with(
            f"{base_urls['order']}/create",
            json=order_data,
            allow_redirects=False,
        )

    def test_create_order_user_not_found_with_services(
        self,
        base_urls,
        sample_items,
        skip_if_services_down,
    ):
        """Pedido associado a usuario inexistente."""
        skip_if_services_down("user", "order")

        order_data = {
            "user_email": "naoexiste@teste.com",
            **sample_items,
        }

        response = requests.post(
            f"{base_urls['order']}/create",
            json=order_data,
            allow_redirects=False,
            timeout=5,
        )

        assert response.status_code in (400, 404)


class TestServiceHealthCheck:

    def test_order_service_health_check(self, base_urls):
        """Verifica a disponibilidade do servico de pedidos."""
        try:
            response = requests.get(
                f"{base_urls['order']}/",
                timeout=2,
            )
        except requests.exceptions.RequestException:
            pytest.skip("Servico de pedidos indisponivel")

        assert response.status_code in (200, 302, 404)

    def test_user_service_health_check(self, base_urls):
        """Verifica a disponibilidade do servico de usuarios."""
        try:
            response = requests.get(
                f"{base_urls['user']}/",
                timeout=2,
            )
        except requests.exceptions.RequestException:
            pytest.skip("Servico de usuarios indisponivel")

        assert response.status_code in (200, 302, 404)