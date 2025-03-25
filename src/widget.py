from datetime import datetime
from typing import Optional
from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    """Маскирует номер карты или счета в зависимости от типа.

    Args:
        info: Строка с типом и номером (например: "Visa Platinum 1234567890123456"
              или "Счет 12345678901234567890")

    Returns:
        Замаскированная строка или сообщение об ошибке
    """
    if not isinstance(info, str) or not info.strip():
        return "Некорректные входные данные"

    try:
        if info.startswith("Счет"):
            parts = info.split()
            if len(parts) < 2:
                return "Некорректный формат счета"
            masked = get_mask_account(parts[-1])
            return f"Счет {masked}" if not masked.startswith("**") else masked
        else:
            parts = info.rsplit(" ", 1)
            if len(parts) < 2:
                return "Некорректный формат карты"
            masked = get_mask_card_number(parts[1])
            if any(word in masked.lower() for word in ["некорректный", "ошибка"]):
                return masked
            return f"{parts[0]} {masked}"
    except Exception as e:
        return f"Ошибка обработки: {str(e)}"


def get_date(date_str: str) -> Optional[str]:
    """Преобразует строку с датой в формате ISO в формат ДД.ММ.ГГГГ.

    Args:
        date_str: Строка с датой в формате ISO (например: "2024-03-11T02:26:18.671407")

    Returns:
        Строка с датой в формате ДД.ММ.ГГГГ или None в случае ошибки
    """
    if not isinstance(date_str, str) or not date_str.strip():
        return None

    try:
        normalized_date = date_str.replace("Z", "") if date_str.endswith("Z") else date_str
        date_obj = datetime.fromisoformat(normalized_date)
        return date_obj.strftime("%d.%m.%Y")
    except (ValueError, TypeError):
        return None
