import unittest

from models.user_model import UserModel


class TestUserModelAlura(unittest.TestCase):

    def setUp(self):
        self.user_data = UserModel(
            email="teste@exemplo.com",
            name="Test User",
            address="123 Test St",
            role="cliente"
        )

    def tearDown(self):
        self.user_data = None

    def test_to_dict(self):
        expected = {
            "email": "teste@exemplo.com",
            "name": "Test User",
            "address": "123 Test St",
            "role": "cliente"
        }

        self.assertEqual(self.user_data.to_dict(), expected)

    def test_serialize_user_incompleto(self):
        result = self.user_data.serialize()

        self.assertEqual(result["email"], "teste@exemplo.com")
        self.assertEqual(result["name"], "Test User")
        self.assertNotIn("password", result)

    def test_assert_raises_example(self):
        def raise_error():
            raise ValueError("This is a test error")

        with self.assertRaises(ValueError):
            raise_error()


if __name__ == "__main__":
    unittest.main()