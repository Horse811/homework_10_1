from typing import List, Dict, Literal

def filter_by_state(operations: List[Dict], state: Literal["EXECUTED", "PENDING"]) -> List[Dict]:
    """Фильтрует операции по статусу."""
    if not operations:
        return []
    return [op for op in operations if op.get("state") == state]

def sort_by_date(operations: List[Dict], reverse: bool = True) -> List[Dict]:
    """Сортирует операции по дате."""
    if not operations:
        return []
    return sorted(
        operations,
        key=lambda x: x["date"],
        reverse=reverse
    )