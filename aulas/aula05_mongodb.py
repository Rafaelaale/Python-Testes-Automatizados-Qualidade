"""Aula 05 - MongoDB: conexao e operacoes CRUD."""

import uuid
from pathlib import Path

from dotenv import dotenv_values
from pymongo import MongoClient

ROOT = Path(__file__).resolve().parents[1]

ENV_FILE = (
    ROOT
    / "burger-app"
    / "burguer-app"
    / "auth-service"
    / ".env"
)


def conectar():
    configuracao = dotenv_values(ENV_FILE)
    uri = configuracao.get("MONGO_URI")

    if not uri:
        raise RuntimeError("MONGO_URI nao configurada.")

    cliente = MongoClient(
        uri,
        serverSelectionTimeoutMS=5000,
    )

    cliente.admin.command("ping")
    return cliente


def executar_aula():
    identificador = str(uuid.uuid4())

    with conectar() as cliente:
        banco = cliente["burguer_app_db"]
        colecao = banco["aula05_exercicios"]

        print("1. Conexao MongoDB: OK")

        try:
            colecao.insert_one(
                {
                    "identificador": identificador,
                    "produto": "Hamburguer",
                    "quantidade": 1,
                    "status": "criado",
                }
            )

            documento = colecao.find_one(
                {"identificador": identificador}
            )

            assert documento is not None
            assert documento["produto"] == "Hamburguer"
            print("2. Insercao e leitura: OK")

            colecao.update_one(
                {"identificador": identificador},
                {"$set": {"status": "atualizado"}},
            )

            atualizado = colecao.find_one(
                {"identificador": identificador}
            )

            assert atualizado["status"] == "atualizado"
            print("3. Atualizacao: OK")

        finally:
            colecao.delete_one(
                {"identificador": identificador}
            )

            print("4. Exclusao do registro de teste: OK")

        print("AULA 05 - CRUD VALIDADO")


if __name__ == "__main__":
    executar_aula()
