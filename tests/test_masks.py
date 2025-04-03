import unittest
from parameterized import parameterized
from src.masks import get_mask_card_number, get_mask_account


class TestMasks(unittest.TestCase):
    @parameterized.expand([
        ("Visa_16_digits", "1234567890123456", "1234 56** **** 3456"),
        ("Mastercard_16_digits", "9876543210987654", "9876 54** **** 7654"),
        ("Min_account_4_digits", "1234", "**1234"),
        ("Standard_account_8_digits", "12345678", "**5678"),
    ])
    def test_valid_masks(self, _, input_num, expected):
        if len(input_num) == 16:
            self.assertEqual(get_mask_card_number(input_num), expected)
        else:
            self.assertEqual(get_mask_account(input_num), expected)

    @parameterized.expand([
        ("Too_short_card", "123"),
        ("Empty_string", ""),
        ("Non_digits", "abcdefghijklmnop"),
    ])
    def test_invalid_input(self, _, input_num):
        with self.assertRaises(ValueError):
            if len(input_num) == 16 or not input_num:
                get_mask_card_number(input_num)
            else:
                get_mask_account(input_num)


if __name__ == "__main__":
    unittest.main()
