import pytest


@pytest.mark.usefixtures("test_db")
def test_insert_user(test_db):
    user = {
        "email": "teste@exemplo.com",
        "name": "Teste Usuário",
    }

    result = test_db["users"].insert_one(user)

    assert result.inserted_id is not None

    encontrado = test_db["users"].find_one({
        "_id": result.inserted_id
    })

    assert encontrado is not None
    assert encontrado["email"] == user["email"]
    assert encontrado["email"] == "teste@exemplo.com"
    assert encontrado["name"] == "Teste Usuário"