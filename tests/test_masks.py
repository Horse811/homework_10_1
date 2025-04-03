import unittest
from parameterized import parameterized
from src.masks import get_mask_card_number, get_mask_account

class TestMasks(unittest.TestCase):
    @parameterized.expand([
        ("Visa 16 цифр", "1234567890123456", "1234 56** **** 3456"),
        ("Mastercard 16 цифр", "9876543210987654", "9876 54** **** 7654"),
        ("Мир 16 цифр", "0000111122223333", "0000 11** **** 3333")
    ])
    def test_mask_card_number_valid(self, _, input_num, expected):
        self.assertEqual(get_mask_card_number(input_num), expected)

    @parameterized.expand([
        ("Короткий счет 4 цифры", "1234", "**1234"),
        ("Стандартный счет 8 цифр", "12345678", "**5678"),
        ("Длинный счет 12 цифр", "123456789012", "**9012")
    ])
    def test_mask_account_valid(self, _, input_num, expected):
        self.assertEqual(get_mask_account(input_num), expected)

    @parameterized.expand([
        ("Слишком короткая карта", "123", "16 цифр"),
        ("Не цифры", "abcdefghijklmnop", "16 цифр"),
        ("Пустая строка", "", "16 цифр")
    ])
    def test_mask_card_number_invalid(self, _, input_num, expected_msg):
        with self.assertRaises(ValueError) as context:
            get_mask_card_number(input_num)
        self.assertIn(expected_msg, str(context.exception))