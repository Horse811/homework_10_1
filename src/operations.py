import re
from collections import Counter
from typing import List, Dict, Pattern


def filter_transactions_by_description(
        transactions: List[Dict],
        search_pattern: str
) -> List[Dict]:
    """
    Фильтрует транзакции по наличию строки в описании с использованием регулярных выражений.

    Args:
        transactions: Список словарей с транзакциями
        search_pattern: Строка для поиска в описании (может быть regex)

    Returns:
        Отфильтрованный список транзакций, где description содержит search_pattern
    """
    try:
        pattern: Pattern = re.compile(search_pattern, re.IGNORECASE)
        return [
            transaction
            for transaction in transactions
            if "description" in transaction
               and pattern.search(transaction["description"])
        ]
    except re.error:
        return []


def count_transactions_by_category(
        transactions: List[Dict],
        categories: List[str]
) -> Dict[str, int]:
    """
    Подсчитывает количество операций по категориям.

    Args:
        transactions: Список словарей с транзакциями
        categories: Список категорий для подсчета

    Returns:
        Словарь с количеством операций по каждой категории
    """
    descriptions = [
        transaction.get("description", "").lower()
        for transaction in transactions
    ]

    category_counts = Counter()

    for category in categories:
        category_lower = category.lower()
        category_counts[category] = sum(
            1 for desc in descriptions
            if category_lower in desc
        )

    return dict(category_counts)
