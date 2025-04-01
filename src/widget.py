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


from datetime import datetime


def get_date(date_str: str) -> str:
    """Преобразует дату из формата 'YYYY-MM-DDThh:mm:ss.sss' в 'DD.MM.YYYY'.
    Вызывает ValueError для пустых строк или некорректных форматов."""
    if not date_str:
        raise ValueError("Дата не может быть пустой строкой")

    try:
        # Пытаемся распарсить дату (обрезаем до 19 символов, чтобы игнорировать миллисекунды)
        dt = datetime.strptime(date_str[:19], "%Y-%m-%dT%H:%M:%S")
        return dt.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты. Ожидается 'YYYY-MM-DDThh:mm:ss...'")
