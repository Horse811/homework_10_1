import unittest
from src.widget import mask_account_card, get_date

class TestWidget(unittest.TestCase):
    # Параметризованные тесты для mask_account_card
    def test_mask_account_card(self):
        self.assertEqual(mask_account_card("1234567890123456"), "1234 56** **** 3456")  # Карта
        self.assertEqual(mask_account_card("12345678"), "**5678")  # Счёт

    def test_mask_account_card_invalid(self):
        with self.assertRaises(ValueError):
            mask_account_card("")  # Пустые данные
        with self.assertRaises(ValueError):
            mask_account_card("abc")  # Не цифры

    # Тесты для get_date
    def test_get_date(self):
        self.assertEqual(get_date("2023-12-31T23:59:59.999"), "31.12.2023")
        self.assertEqual(get_date("2021-01-01T00:00:00.000"), "01.01.2021")

    def test_get_date_invalid(self):
        with self.assertRaises(ValueError):  # Ожидаем ValueError для пустой строки
            get_date("")
        with self.assertRaises(ValueError):  # Ожидаем ValueError для неполной даты
            get_date("2023")

if __name__ == "__main__":
    unittest.main()
