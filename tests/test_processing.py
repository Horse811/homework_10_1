import unittest
from parameterized import parameterized
from src.processing import filter_by_state, sort_by_date


class TestProcessing(unittest.TestCase):
    def setUp(self):
        self.operations = [
            {"id": 1, "state": "EXECUTED", "date": "2023-12-31T23:59:59.999"},
            {"id": 2, "state": "PENDING", "date": "2022-01-01T00:00:00.000"},
            {"id": 3, "state": "EXECUTED", "date": "2021-06-15T12:30:45.000"},
        ]

    @parameterized.expand([
        ("EXECUTED", [1, 3]),
        ("PENDING", [2]),
        ("CANCELED", []),
    ])
    def test_filter_by_state(self, state, expected_ids):
        result = filter_by_state(self.operations, state)
        self.assertEqual([op["id"] for op in result], expected_ids)

    @parameterized.expand([
        (True, [1, 2, 3]),   # По убыванию даты
        (False, [3, 2, 1]),  # По возрастанию даты
    ])
    def test_sort_by_date(self, reverse, expected_order):
        result = sort_by_date(self.operations, reverse=reverse)
        self.assertEqual([op["id"] for op in result], expected_order)


if __name__ == "__main__":
    unittest.main()
