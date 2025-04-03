import unittest
from parameterized import parameterized
from src.widget import mask_account_card, get_date


class TestWidget(unittest.TestCase):
    @parameterized.expand([
        ("Card_number", "1234567890123456", "1234 56** **** 3456"),
        ("Account_number", "12345678", "**5678"),
    ])
    def test_mask_account_card(self, _, input_data, expected):
        self.assertEqual(mask_account_card(input_data), expected)

    @parameterized.expand([
        ("Valid_date_1", "2023-12-31T23:59:59.999", "31.12.2023"),
        ("Valid_date_2", "2021-01-01T00:00:00.000", "01.01.2021"),
    ])
    def test_get_date_valid(self, _, input_date, expected):
        self.assertEqual(get_date(input_date), expected)

    @parameterized.expand([
        ("Empty_string", ""),
        ("Invalid_format", "2023"),
        ("Non_date_string", "not-a-date"),
    ])
    def test_get_date_invalid(self, _, input_date):
        with self.assertRaises(ValueError):
            get_date(input_date)


if __name__ == "__main__":
    unittest.main()
