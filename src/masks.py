def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и возвращает маску номера.

    Формат маски: XXXX XX** **** XXXX

    Args:
        card_number: Номер карты (может содержать пробелы/разделители)

    Returns:
        Маскированный номер карты или сообщение об ошибке
    """
    if not isinstance(card_number, str) or not card_number.strip():
        return "Некорректный номер карты"

    cleaned_number = "".join(c for c in card_number if c.isdigit())

    if len(cleaned_number) != 16:
        return "Номер карты должен содержать 16 цифр"

    return f"{cleaned_number[:4]} {cleaned_number[4:6]}** **** {cleaned_number[-4:]}"


def get_mask_account(account_number: str) -> str:
    """Функция принимает на вход номер счета и возвращает маску номера.

    Формат маски: **XXXX

    Args:
        account_number: Номер счета (может содержать пробелы/разделители)

    Returns:
        Маскированный номер счета или сообщение об ошибке
    """
    if not isinstance(account_number, str) or not account_number.strip():
        return "Некорректный номер счета"

    cleaned_number = "".join(c for c in account_number if c.isdigit())

    if len(cleaned_number) != 20:
        return "Номер счета должен содержать 20 цифр"

    return f"**{cleaned_number[-4:]}"
