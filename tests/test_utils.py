import json
from unittest.mock import mock_open, patch
import pytest
from src.utils import load_transactions


@pytest.fixture
def sample_transactions():
    return [
        {"id": 1, "amount": 100, "currency": "RUB"},
        {"id": 2, "amount": 50, "currency": "USD"}
    ]


def test_load_valid_file(tmp_path, sample_transactions):
    file = tmp_path / "transactions.json"
    file.write_text(json.dumps(sample_transactions))
    assert load_transactions(str(file)) == sample_transactions


def test_load_empty_file(tmp_path):
    file = tmp_path / "empty.json"
    file.touch()
    assert load_transactions(str(file)) == []


def test_load_nonexistent_file():
    assert load_transactions("nonexistent.json") == []


@patch('builtins.open', mock_open(read_data='invalid json'))
def test_load_invalid_json():
    assert load_transactions("bad.json") == []


def test_load_non_list_content(tmp_path):
    file = tmp_path / "not_list.json"
    file.write_text(json.dumps({"key": "value"}))
    assert load_transactions(str(file)) == []
