import unittest
from parameterized import parameterized
from src.masks import get_mask_card_number, get_mask_account


class TestMasks(unittest.TestCase):
    @parameterized.expand([
        ("Visa 16 цифр", "1234567890123456", "1234 56** **** 3456"),
        ("Mastercard 16 цифр", "9876543210987654", "9876 54** **** 7654"),
    ])
    def test_mask_card_number_valid(self, _, input_num, expected):
        self.assertEqual(get_mask_card_number(input_num), expected)

    @parameterized.expand([
        ("Счет 8 цифр", "12345678", "**5678"),
        ("Счет 10 цифр", "9876543210", "**3210"),
    ])
    def test_mask_account_valid(self, _, input_num, expected):
        self.assertEqual(get_mask_account(input_num), expected)


if __name__ == "__main__":
    unittest.main()
