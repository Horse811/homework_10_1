import pytest
from src.filter import (
    filter_transactions_by_description,
    count_transactions_by_category,
)


@pytest.fixture
def sample_transactions():
    return [
        {"description": "Payment for groceries", "amount": 100},
        {"description": "Transfer to savings", "amount": 200},
        {"description": "Grocery store payment", "amount": 50},
        {"description": "Salary payment", "amount": 1000},
    ]


def test_filter_transactions_by_description(sample_transactions):
    # Тестирование базового поиска
    result = filter_transactions_by_description(sample_transactions, "payment")
    assert len(result) == 3
    assert all("payment" in t["description"].lower() for t in result)

    # Тестирование регистронезависимого поиска
    result = filter_transactions_by_description(sample_transactions, "PAYMENT")
    assert len(result) == 3

    # Тестирование regex поиска
    result = filter_transactions_by_description(sample_transactions, r"pay.*groceries")
    assert len(result) == 1
    assert result[0]["amount"] == 100

    # Тестирование пустого результата
    result = filter_transactions_by_description(sample_transactions, "non-existent")
    assert len(result) == 0


def test_count_transactions_by_category(sample_transactions):
    categories = ["payment", "transfer", "groceries"]
    result = count_transactions_by_category(sample_transactions, categories)

    assert result["payment"] == 3
    assert result["transfer"] == 1
    assert result["groceries"] == 2

    # Тестирование пустых категорий
    result = count_transactions_by_category(sample_transactions, [])
    assert result == {}
