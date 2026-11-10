import pytest


class ResultadoInsercao:
    def __init__(self, inserted_id):
        self.inserted_id = inserted_id


class ColecaoUsuarios:
    def __init__(self):
        self.registros = {}
        self.proximo_id = 1

    def insert_one(self, usuario):
        identificador = self.proximo_id
        self.proximo_id += 1
        self.registros[identificador] = {
            **usuario,
            "_id": identificador,
        }
        return ResultadoInsercao(identificador)

    def find_one(self, filtro):
        return self.registros.get(filtro.get("_id"))


@pytest.fixture(scope="session")
def cliente_db():
    print("\nSETUP: criando banco simulado")
    banco = {"users": ColecaoUsuarios()}
    yield banco
    print("\nTEARDOWN: encerrando banco simulado")


@pytest.fixture
def test_db(cliente_db):
    cliente_db["users"].registros.clear()
    cliente_db["users"].proximo_id = 1
    return cliente_db