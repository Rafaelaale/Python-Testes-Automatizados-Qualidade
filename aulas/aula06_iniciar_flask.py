"""Aula 06 - Inicializacao dos microservicos Flask."""

import contextlib
import importlib
import io
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
APP = ROOT / "burger-app" / "burguer-app"

SERVICES = {
    "auth-service": 5000,
    "user-service": 5001,
    "order-service": 5002,
    "product-service": 5003,
}


def main():
    if len(sys.argv) != 2:
        raise SystemExit(
            "Uso: python aula06_iniciar_flask.py SERVICO"
        )

    service = sys.argv[1]

    if service not in SERVICES:
        raise SystemExit("Microservico desconhecido.")

    folder = APP / service

    os.chdir(folder)
    sys.path.insert(0, str(folder))

    load_dotenv(folder / ".env", override=True)

    if not os.getenv("MONGO_URI"):
        raise RuntimeError("MONGO_URI ausente.")

    if not os.getenv("SECRET_KEY"):
        raise RuntimeError("SECRET_KEY ausente.")

    # Evita exibir a chave secreta que o codigo
    # original imprime durante a importacao.
    with contextlib.redirect_stdout(io.StringIO()):
        module = importlib.import_module("app")

    print(
        f"SERVICO: {service} "
        f"PORTA: {SERVICES[service]}",
        flush=True,
    )

    module.app.run(
        host="127.0.0.1",
        port=SERVICES[service],
        debug=False,
        use_reloader=False,
    )


if __name__ == "__main__":
    main()
