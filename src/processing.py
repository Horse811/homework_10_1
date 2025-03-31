from datetime import datetime
from typing import List, Dict, Optional


def filter_by_state(operations: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """
    Фильтрует список операций по указанному статусу.

    Args:
        operations: Список словарей с операциями
        state: Статус для фильтрации (по умолчанию "EXECUTED")

    Returns:
        Отфильтрованный список операций

    Raises:
        ValueError: Если operations не является списком
    """
    if not isinstance(operations, list):
        raise ValueError("Operations должен быть списком")

    return [op for op in operations if op.get("state") == state]


def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """
    Сортирует операции по дате.

    Args:
        operations: Список словарей с операциями
        reverse: Порядок сортировки (True - по убыванию, False - по возрастанию)

    Returns:
        Отсортированный список операций

    Raises:
        ValueError: Если operations не содержит поле 'date' или неверный формат даты
    """
    if not operations:
        return []

    try:
        return sorted(
            operations,
            key=lambda x: datetime.strptime(x["date"], "%Y-%m-%dT%H:%M:%S.%f"),
            reverse=reverse
        )
    except KeyError:
        raise ValueError("Один или несколько элементов не содержат поле 'date'")
    except ValueError as e:
        raise ValueError(f"Неверный формат даты: {e}")
