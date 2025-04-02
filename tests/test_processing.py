import sys
import os
import unittest
from datetime import datetime
from src.processing import filter_by_state, sort_by_date  # Убедитесь, что путь правильный

class TestProcessing(unittest.TestCase):
    def setUp(self):
        self.operations = [
            {"id": 1, "state": "EXECUTED", "date": "2023-12-31T23:59:59.999"},
            {"id": 2, "state": "PENDING", "date": "2022-01-01T00:00:00.000"},
            {"id": 3, "state": "EXECUTED", "date": "2021-06-15T12:30:45.000"},
        ]

    def test_filter_by_state(self):
        filtered = filter_by_state(self.operations, "EXECUTED")
        self.assertEqual(len(filtered), 2)
        self.assertEqual(filtered[0]["id"], 1)
        self.assertEqual(filtered[1]["id"], 3)

    def test_sort_by_date_desc(self):
        sorted_ops = sort_by_date(self.operations)
        self.assertEqual(sorted_ops[0]["id"], 1)
        self.assertEqual(sorted_ops[1]["id"], 2)
        self.assertEqual(sorted_ops[2]["id"], 3)

    def test_sort_by_date_asc(self):
        sorted_ops = sort_by_date(self.operations, reverse=False)
        self.assertEqual(sorted_ops[0]["id"], 3)
        self.assertEqual(sorted_ops[1]["id"], 2)
        self.assertEqual(sorted_ops[2]["id"], 1)

    def test_filter_by_state_empty(self):
        result = filter_by_state([], "EXECUTED")
        self.assertEqual(result, [])

    def test_sort_by_date_empty(self):
        result = sort_by_date([])
        self.assertEqual(result, [])
if __name__ == '__main__':
    unittest.main()
