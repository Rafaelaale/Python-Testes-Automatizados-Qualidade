"""Testes estruturais dos quatro microservicos do Burger App."""

import ast
from pathlib import Path

import pytest

ROOT = (
    Path(__file__).resolve().parents[1]
    / "burger-app"
    / "burguer-app"
)

SERVICES = {
    "auth-service": 5000,
    "user-service": 5001,
    "order-service": 5002,
    "product-service": 5003,
}


@pytest.mark.parametrize("service", SERVICES)
def test_microservico_possui_arquivos_essenciais(service):
    folder = ROOT / service

    assert (folder / "app.py").is_file()
    assert (folder / "requirements.txt").is_file()


@pytest.mark.parametrize("service", SERVICES)
def test_aplicacao_possui_sintaxe_python_valida(service):
    app_file = ROOT / service / "app.py"

    source = app_file.read_text(encoding="utf-8-sig")

    tree = ast.parse(source, filename=str(app_file))

    assert isinstance(tree, ast.Module)
    assert any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "Flask"
        for node in ast.walk(tree)
    )


@pytest.mark.parametrize("service", SERVICES)
def test_microservico_possui_dependencias(service):
    requirements = ROOT / service / "requirements.txt"

    dados = requirements.read_bytes()

    if dados.startswith((b"\xff\xfe", b"\xfe\xff")):
        packages = dados.decode("utf-16").lower()
    elif dados.startswith(b"\xef\xbb\xbf"):
        packages = dados.decode("utf-8-sig").lower()
    else:
        packages = dados.decode("utf-8").lower()

    assert "flask" in packages
    assert "pymongo" in packages
    assert "python-dotenv" in packages


@pytest.mark.parametrize("service", SERVICES)
def test_configuracao_local_existe(service):
    env_file = ROOT / service / ".env"

    assert env_file.is_file()

    content = env_file.read_text(encoding="utf-8")

    assert "MONGO_URI=" in content
    assert "SECRET_KEY=" in content


@pytest.mark.parametrize("service,port", SERVICES.items())
def test_porta_do_servico_documentada(service, port):
    app_file = ROOT / service / "app.py"

    source = app_file.read_text(encoding="utf-8-sig")

    assert f"port={port}" in source
