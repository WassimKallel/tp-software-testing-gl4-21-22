from app import calculate_factorial, get_user
from unittest import TestCase, main
from unittest.mock import patch


class TestApp(TestCase):
    def test_hello(self):
        assert "hello" == "hello"

    def test_factorial(self):
        assert calculate_factorial(3) == 6

    @patch("app.sqlite3")
    def test_get_user(self, mock_class):
        # given
        mock_class.connect().execute().fetchone.return_value = (1, 'wassim')

        expected_user = {
            "user_id": 1,
            "name": "wassim"
        }

        # when
        item = get_user(1)

        # then
        assert item == expected_user


if __name__ == '__main__':
    main()
