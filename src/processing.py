def filter_by_state(operations: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param operations: Список словарей с данными операций.
    :param state: Значение ключа 'state' для фильтрации (по умолчанию 'EXECUTED').
    :return: Отфильтрованный список словарей.
    """
    return [operation for operation in operations if operation.get('state') == state]


def sort_by_date(operations: list[dict], reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по ключу 'date'.

    :param operations: Список словарей с данными операций.
    :param reverse: Флаг сортировки по убыванию (по умолчанию True).
    :return: Отсортированный список словарей.
    """
    return sorted(operations, key=lambda x: x['date'], reverse=reverse)
