from datetime import datetime
from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(data: str) -> str:
    """Маскирует номер карты или счета"""
    if not data:
        raise ValueError("Пустые входные данные")
    if len(data) == 16 and data.isdigit():
        return get_mask_card_number(data)
    elif len(data) >= 4 and data.isdigit():
        return get_mask_account(data)
    raise ValueError("Некорректный формат данных")


def get_date(date_str: str) -> str:
    """Преобразует дату из формата ISO в DD.MM.YYYY"""
    if not date_str:
        raise ValueError("Дата не может быть пустой строкой")
    try:
        dt = datetime.strptime(date_str[:19], "%Y-%m-%dT%H:%M:%S")
        return dt.strftime("%d.%m.%Y")
    except ValueError as e:
        raise ValueError("Неверный формат даты. Ожидается 'YYYY-MM-DDThh:mm:ss...'") from e
