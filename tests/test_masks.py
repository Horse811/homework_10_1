import unittest
from src.masks import get_mask_card_number, get_mask_account

class TestMasks(unittest.TestCase):
    # Тесты для get_mask_card_number
    def test_mask_card_number(self):
        self.assertEqual(get_mask_card_number("1234567890123456"), "1234 56** **** 3456")
        self.assertEqual(get_mask_card_number("9876543210987654"), "9876 54** **** 7654")

    def test_mask_card_number_invalid(self):
        with self.assertRaises(ValueError):
            get_mask_card_number("123")  # Слишком короткий номер
        with self.assertRaises(ValueError):
            get_mask_card_number("")  # Пустая строка

    # Тесты для get_mask_account
    def test_mask_account(self):
        self.assertEqual(get_mask_account("12345678"), "**5678")
        self.assertEqual(get_mask_account("9876543210"), "**3210")

    def test_mask_account_invalid(self):
        with self.assertRaises(ValueError):
            get_mask_account("12")  # Слишком короткий номер
        with self.assertRaises(ValueError):
            get_mask_account("")  # Пустая строка

if __name__ == "__main__":
    unittest.main()