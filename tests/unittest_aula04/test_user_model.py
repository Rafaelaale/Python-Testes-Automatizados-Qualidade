import unittest

from models.user_model import UserModel


class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.usuario = UserModel(
            email="teste@exemplo.com",
            name="Usuario Teste",
            address="Salvador",
        )

    def tearDown(self):
        self.usuario = None

    def test_role_padrao(self):
        self.assertEqual(self.usuario.role, "cliente")

    def test_serializacao(self):
        resultado = self.usuario.serialize()
        self.assertEqual(resultado["email"], "teste@exemplo.com")
        self.assertEqual(resultado["name"], "Usuario Teste")

    def test_conversao_dicionario(self):
        resultado = self.usuario.to_dict()
        self.assertIsInstance(resultado, dict)
        self.assertEqual(resultado["address"], "Salvador")

    def test_criacao_por_dicionario(self):
        dados = {
            "email": "novo@exemplo.com",
            "name": "Novo Usuario",
        }

        usuario = UserModel.from_dict(dados)

        self.assertEqual(usuario.email, "novo@exemplo.com")
        self.assertEqual(usuario.role, "cliente")

    def test_campos_padrao_na_serializacao(self):
        resultado = self.usuario.serialize({
            "email": "outro@exemplo.com"
        })

        self.assertEqual(resultado["name"], "")
        self.assertEqual(resultado["role"], "cliente")

    def test_tipo_invalido(self):
        with self.assertRaises(AttributeError):
            UserModel.from_dict(None)


if __name__ == "__main__":
    unittest.main()