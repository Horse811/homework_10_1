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
        ("EXECUTED_state", "EXECUTED", [1, 3]),
        ("PENDING_state", "PENDING", [2]),
        ("CANCELED_state", "CANCELED", []),
    ])
    def test_filter_by_state(self, _, state, expected_ids):
        result = filter_by_state(self.operations, state)
        self.assertEqual([op["id"] for op in result], expected_ids)

    @parameterized.expand([
        ("Descending_sort", True, [1, 2, 3]),
        ("Ascending_sort", False, [3, 2, 1]),
    ])
    def test_sort_by_date(self, _, reverse, expected_order):
        result = sort_by_date(self.operations, reverse=reverse)
        self.assertEqual([op["id"] for op in result], expected_order)

    def test_empty_input(self):
        self.assertEqual(filter_by_state([], "EXECUTED"), [])
        self.assertEqual(sort_by_date([]), [])


if __name__ == "__main__":
    unittest.main()
