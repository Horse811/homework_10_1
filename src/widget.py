from datetime import datetime

from masks import get_mask_account
from masks import get_mask_card_number


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета в зависимости от типа.
    Принимает строку с типом и номером, возвращает замаскированную строку.
    """
    if info.startswith("Счет"):
        # Обработка счета
        account_number = info.split(" ")[-1]
        masked_info = f"Счет {get_mask_account(account_number)}"
    else:
        # Обработка карты
        card_parts = info.rsplit(" ", 1)  # Разделяем на тип карты и номер
        card_type = card_parts[0]
        card_number = card_parts[1]
        masked_info = f"{card_type} {get_mask_card_number(card_number)}"
    return masked_info


def get_date(date_str: str) -> str:
    """
    Преобразует строку с датой в формате "2024-03-11T02:26:18.671407"
    в строку с датой в формате "ДД.ММ.ГГГГ".
    """
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%d.%m.%Y")
