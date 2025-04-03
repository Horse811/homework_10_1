import unittest
from parameterized import parameterized
from src.widget import mask_account_card, get_date


class TestWidget(unittest.TestCase):
    """Тесты для модуля widget.py"""

    # Параметризованные тесты маскирования
    @parameterized.expand([
        ("Карта", "1234567890123456", "1234 56** **** 3456"),
        ("Счет", "12345678", "**5678")
    ])
    def test_mask_account_card(self, _, input_data, expected):
        self.assertEqual(mask_account_card(input_data), expected)

    # Параметризованные тесты дат
    @parameterized.expand([
        ("Стандартная дата", "2023-12-31T23:59:59.999", "31.12.2023"),
        ("Короткая дата", "2021-01-01T00:00:00.000", "01.01.2021")
    ])
    def test_get_date_valid(self, _, input_date, expected):
        self.assertEqual(get_date(input_date), expected)

    # Тесты для невалидных данных
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            mask_account_card("abc")
        with self.assertRaises(ValueError):
            get_date("2023")


if __name__ == "__main__":
    unittest.main()