from src.masks import get_mask_card_number, get_mask_account  # Изменено здесь

def mask_account_card(data: str) -> str:
    if not data:
        raise ValueError("Пустые входные данные")
    if len(data) == 16 and data.isdigit():
        return get_mask_card_number(data)
    elif len(data) >= 4 and data.isdigit():
        return get_mask_account(data)
    else:
        raise ValueError("Некорректный формат данных")

def get_date(date_str: str) -> str:
    """Преобразует дату из формата 'YYYY-MM-DDTHH:MM:SS.SSS' в 'DD.MM.YYYY'."""
    if not date_str:
        raise ValueError("Пустая строка даты")
    try:
        return f"{date_str[8:10]}.{date_str[5:7]}.{date_str[:4]}"
    except IndexError:
        raise IndexError("Неполная дата") from None
